from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from app import db
import os
from app.Hautomotor import bp
#from app.auth.forms import LoginForm, RegistrationForm
from app.models import HojaAutomotor
from app.Hautomotor.forms import CrearHVAForm
from werkzeug.utils import secure_filename
from datetime import datetime
from hashlib import md5
# from app.auth.email import send_password_reset_email


UPLOAD_FOLDER = '/home/camilo/projects/alcaldia/Files/ParqueAutomotor'
IMAGES_EXTENSIONS = ['.jpg', '.png', '.gif']

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in IMAGES_EXTENSIONS

@bp.route('/crear', methods=['GET', 'POST'])
@login_required

def crear_HVA():
    form = CrearHVAForm()
    if form.validate_on_submit():
        hvautomotor = HojaAutomotor(
            descripcion=form.descripcion.data,
            placa=form.placa.data,
            propietario=form.propietario.data,
            identificacion_interna=form.identificacion.data,
            tarjeta_propiedad=form.tarjeta.data,
            fecha_expedicion=form.fecha_expedicion.data,
            avaluo=form.avaluo.data,
            seccion=form.seccion.data,
            clase_vehiculo=form.clase_vehiculo.data,
            marca=form.marca.data,
            combustible=form.combustible.data,
            modelo=form.modelo.data,
            cilindraje=form.cilindraje.data,
            color=form.color.data,
            numero_motor=form.numero_motor.data,
            numero_serie=form.numero_serie.data,
            numero_chasis=form.numero_chasis.data,
            tipo_caja=form.tipo_caja.data,
            capacidad=form.capacidad.data,
        )
        if form.tarjeta_propiedad.data:
            print('Hay informacion en el formulario tarjtea de propiedad')
            tarjeta_propiedad=request.files[form.tarjeta_propiedad.name]
            if tarjeta_propiedad.filename == '':
                flash('No selecciono ningun archivo')
                print('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(tarjeta_propiedad.filename)[1]
            print(file_ext)
            if tarjeta_propiedad and file_ext in IMAGES_EXTENSIONS:
                print('Procensando archivos tarjeta propiedad')
                filename = secure_filename(tarjeta_propiedad.filename)
                hvautomotor.filename_tarjeta_propiedad=filename
                hvautomotor.path_tarjeta_propiedad=os.path.join(UPLOAD_FOLDER, filename)
                filename, file_extension = os.path.splitext(filename)
                filenamehash = str(datetime.now())+filename
                filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                tarjeta_propiedad.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                print('Archivo guardado con exito')
        db.session.add(hvautomotor)
        db.session.commit()
        flash('Hoja de vida Guardada con exito') 
        return redirect(url_for('Hautomotor.crear_HVA'))

    return render_template('Hautomotor/crear.html', form=form)

@bp.route('/visualizar', methods=['GET', 'POST'])
@login_required

def visualizar_HVA():
    # hojas_de_vida = Hojaobra.query.order_by(Hojaobra.fecha_ultima_actualizacion.desc())
    # return render_template('HVObra/visualizar.html',hojas_vida=hojas_de_vida)
    pass