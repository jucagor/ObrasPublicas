from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from app import db
from app.HVObra import bp
#from app.auth.forms import LoginForm, RegistrationForm
from app.models import Hojaobra
from app.HVObra.forms import CrearHVOForm
# from app.auth.email import send_password_reset_email


UPLOAD_FOLDER = '/home/camilo/projects/alcaldia/Files'

@bp.route('/crear', methods=['GET', 'POST'])
@login_required

def crear_HVO():
    form = CrearHVOForm()
    if form.validate_on_submit():
        hv = Hojaobra(fecha_recibido=form.fecha_recibido.data,
                    descripcion=form.descripcion.data, peticionario=form.peticionario.data,
                    fecha_respuesta=form.fecha_respuesta.data)
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
        return redirect(url_for('HVObra.crear_HVO'))
    return render_template('HVObra/crear.html', form=form)

@bp.route('/visualizar', methods=['GET', 'POST'])
@login_required

def visualizar_HVO():
    hojas_de_vida = Hojaobra.query.order_by(Hojaobra.fecha_ultima_actualizacion.desc())
    return render_template('HVObra/visualizar.html',hojas_vida=hojas_de_vida)
