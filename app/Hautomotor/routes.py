from flask import render_template, redirect, url_for, flash, request, send_from_directory
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
    id_automotor = request.args.get('id',None)
    if id_automotor is not None:
        #Consulto el vehiculo en la base de datos
        automotor=HojaAutomotor.query.filter_by(id=id_automotor).first()
        #Lleno el formulario con los datos del vehiculo
        form.placa.data=automotor.placa
        form.descripcion.data=automotor.descripcion
        form.propietario.data=automotor.propietario
        form.identificacion.data=automotor.identificacion_interna
        form.tarjeta.data=automotor.tarjeta_propiedad
        form.fecha_expedicion.data=automotor.fecha_expedicion
        form.avaluo.data=automotor.avaluo
        form.seccion.data=automotor.seccion
        form.clase_vehiculo.data=automotor.clase_vehiculo
        form.marca.data=automotor.marca
        form.combustible.data=automotor.combustible
        form.modelo.data=automotor.modelo
        form.cilindraje.data=automotor.cilindraje
        form.color.data=automotor.color
        form.numero_motor.data=automotor.numero_motor
        form.numero_serie.data=automotor.numero_serie
        form.numero_chasis.data=automotor.numero_chasis
        form.tipo_caja.data=automotor.tipo_caja
        form.capacidad.data=automotor.capacidad

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
                    hvautomotor.path_foto1=os.path.join('/home/camilo/projects/alcaldia/obraspublicas/app/static', filename)

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
    hvautomotor = HojaAutomotor.query.order_by(HojaAutomotor.placa.asc())
    return render_template('Hautomotor/visualizar.html',hvautomotor=hvautomotor,image_name=image_names)


@bp.route('/detalles/<value>', methods=['GET', 'POST'])
@login_required

def detalles_HVA(value):

    hvautomotor=HojaAutomotor.query.get(value)
    
    context = {
        'hvautomotor':hvautomotor,

    }

    if request.method == 'POST':
        archivo=request.form.get('archivo')
        print(archivo)

        if archivo=="TarjetaPropiedad":
            if hvautomotor.path_tarjeta_propiedad!=None:
                return send_from_directory(UPLOAD_FOLDER,hvautomotor.path_tarjeta_propiedad.split('/')[7],as_attachment=True)
            else:
                flash("No existe este documento!!")

        elif archivo=="Soat":
            if hvautomotor.path_soat!=None:
                return send_from_directory(UPLOAD_FOLDER,hvautomotor.path_soat.split('/')[7],as_attachment=True)
            else:
                flash("No existe este documento!!")

        elif archivo=="TecnoMecanica":
            if hvautomotor.path_tecno!=None:
                return send_from_directory(UPLOAD_FOLDER,hvautomotor.path_tecno.split('/')[7],as_attachment=True)
            else:
                flash("No existe este documento!!")

        elif archivo=="Foto1":
            return send_from_directory('/home/camilo/projects/alcaldia/obraspublicas/app/static',hvautomotor.filename_foto1,as_attachment=True)

        elif archivo=="Foto2":
            if hvautomotor.path_foto2!=None:
                return send_from_directory(UPLOAD_FOLDER,hvautomotor.path_foto2.split('/')[7],as_attachment=True)
            else:
                flash("No existe este documento!!")


    return render_template('Hautomotor/detalles.html',**context)
