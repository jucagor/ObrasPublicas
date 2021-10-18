from flask import render_template, redirect, url_for, flash, request
from werkzeug.utils import secure_filename
import os
from werkzeug.utils import secure_filename
from flask_login import current_user, login_required
from app import db
from app.PQRS import bp
from app.PQRS.forms import CrearPQRForm
from app.models import PQR
from hashlib import md5
from datetime import datetime


UPLOAD_FOLDER = '/home/camilo/projects/alcaldia/Files'

@bp.route('/crear', methods=['GET', 'POST'])
@login_required

def crear_pqr():
    form = CrearPQRForm()
    if form.validate_on_submit():
        pqr = PQR(id=form.numero_pqr.data, fecha_recibido=form.fecha_recibido.data,
                    descripcion=form.descripcion.data, peticionario=form.peticionario.data,
                    fecha_respuesta=form.fecha_respuesta.data, user_id = current_user.username)
        if form.respuesta.data:
            respuesta = request.files[form.respuesta.name]
            if respuesta.filename == '':
                flash('No selecciono ningun archivo')
                
                return redirect(request.url)
            if respuesta:
                filename = secure_filename(respuesta.filename)
                pqr.filename_respuesta = filename
                pqr.path_respuesta = os.path.join(UPLOAD_FOLDER, filename)
                filename, file_extension = os.path.splitext(filename)
                #Creo un nombre unico, con el Filename y el tiempo actual
                filename = str(datetime.now())+filename
                #Hasheo el nombre del archivo
                filename = md5(filename.encode('utf-8')).hexdigest()+file_extension
                respuesta.save(os.path.join(UPLOAD_FOLDER, filename))
        db.session.add(pqr)
        db.session.commit()
        flash('PQR Guardada con exito')  
        return redirect(url_for('PQRS.crear_pqr'))
    return render_template('PQRS/crear.html', form=form)


@bp.route('/visualizar', methods=['GET', 'POST'])
@login_required

def visualizar_pqr():
    pqrs = PQR.query.order_by(PQR.fecha_recibido.desc())
    return render_template('PQRS/visualizar.html',pqrs=pqrs)

