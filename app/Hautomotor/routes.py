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
IMAGES_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.pdf', '.JPG', '.JPEG', '.PNG', '.GIF', '.PDF']
image_names = os.listdir(UPLOAD_FOLDER)


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
        #Valido Formulario Tarjeta de Propiedad
        if form.tarjeta_propiedad.data:

            tarjeta_propiedad=request.files[form.tarjeta_propiedad.name]
            if tarjeta_propiedad.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(tarjeta_propiedad.filename)[1]
            if tarjeta_propiedad:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Tarjeta de Propiedad ( JPG PNG GIF PDF )')
                    return redirect(url_for('Hautomotor.crear_HVA'))
                else:                    
                    filename = secure_filename(tarjeta_propiedad.filename)
                    hvautomotor.filename_tarjeta_propiedad=filename
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    tarjeta_propiedad.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    hvautomotor.path_tarjeta_propiedad=os.path.join(UPLOAD_FOLDER, filenamehash)

        #Valido Formulario Tarjeta de Soat
        if form.soat.data:

            soat=request.files[form.soat.name]
            if soat.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(soat.filename)[1]
            if soat:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para SOAT ( JPG PNG PDF )')
                    return redirect(url_for('Hautomotor.crear_HVA'))
                else:                    
                    filename = secure_filename(soat.filename)
                    hvautomotor.filename_soat=filename
                    
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    soat.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    hvautomotor.path_soat=os.path.join(UPLOAD_FOLDER, filenamehash)

        #Valido Formulario Tarjeta de Tecno Mecanica
        if form.tecnomecanica.data:

            tecnomecanica=request.files[form.tecnomecanica.name]
            if tecnomecanica.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(tecnomecanica.filename)[1]
            if tecnomecanica:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Tecno Mecanica ( JPG PNG PDF )')
                    return redirect(url_for('Hautomotor.crear_HVA'))
                else:                    
                    filename = secure_filename(tecnomecanica.filename)
                    hvautomotor.filename_tecno=filename
                    
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    tecnomecanica.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    hvautomotor.path_tecno=os.path.join(UPLOAD_FOLDER, filenamehash)
    
        #Valido Formulario Foto 1
        if form.foto1.data:

            foto1=request.files[form.foto1.name]
            if foto1.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(foto1.filename)[1]
            if foto1:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Foto Frontal ( JPG PNG GIF )')
                    return redirect(url_for('Hautomotor.crear_HVA'))
                else:                    
                    filename = secure_filename(foto1.filename)
                    hvautomotor.filename_foto1=filename
                    
                    foto1.save(os.path.join('/home/camilo/projects/alcaldia/obraspublicas/app/static', filename))
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    foto1.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    print(filenamehash)
                    hvautomotor.path_foto1=os.path.join(UPLOAD_FOLDER, filenamehash)

        #Valido Formulario Foto 2
        if form.foto2.data:

            foto2=request.files[form.foto2.name]
            if foto2.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(foto2.filename)[1]
            if foto2:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Foto Lateral ( JPG PNG GIF )')
                    return redirect(url_for('Hautomotor.crear_HVA'))
                else:                    
                    filename = secure_filename(foto2.filename)
                    hvautomotor.filename_foto2=filename
                    
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    foto2.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    hvautomotor.path_foto2=os.path.join(UPLOAD_FOLDER, filenamehash)
        
        db.session.add(hvautomotor)
        db.session.commit()
        flash('Hoja de vida Guardada con exito') 
        return redirect(url_for('Hautomotor.crear_HVA'))

    return render_template('Hautomotor/crear.html', form=form)

@bp.route('/visualizar', methods=['GET', 'POST'])
@login_required

def visualizar_HVA():
    hvautomotor = HojaAutomotor.query.order_by(HojaAutomotor.fecha_ultima_actualizacion.desc())
    return render_template('Hautomotor/visualizar.html',hvautomotor=hvautomotor,image_name=image_names)
    pass