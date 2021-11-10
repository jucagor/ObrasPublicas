from flask import render_template, redirect, url_for, flash, request, send_from_directory
from flask_login import current_user, login_required
from app import db
import os
from app.InventarioVial import bp
#from app.auth.forms import LoginForm, RegistrationForm
from app.models import inventarioVial
from app.InventarioVial.forms import CrearIVForm
from werkzeug.utils import secure_filename
from datetime import datetime
from hashlib import md5
# from app.auth.email import send_password_reset_email



UPLOAD_FOLDER = '/home/camilo/projects/alcaldia/Files/InventarioVial'
FORMATO_EXTENSIONS = ['.xls', '.xlsx', '.pdf', '.XLS', '.XLSX', '.PDF']
SIG_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.pdf', '.JPG', '.JPEG', '.PNG', '.GIF', '.PDF']
image_names = os.listdir(UPLOAD_FOLDER)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in SIG_EXTENSIONS

@bp.route('/crear', methods=['GET', 'POST'])
@login_required

def crear_IV():
    form = CrearIVForm()
    id_inventario = request.args.get('id',None)
    print(id_inventario)
    print(id_inventario is None)
    if id_inventario is not None:
        #Consulto el vehiculo en la base de datos
        inventario=inventarioVial.query.filter_by(id=id_inventario).first()
        #Lleno el formulario con los datos del vehiculo
        form.fecha_creacion.data=inventario.fecha_creacion
        # form.descripcion.data=automotor.descripcion
        # form.propietario.data=automotor.propietario
        # form.identificacion.data=automotor.identificacion_interna
        # form.tarjeta.data=automotor.formato
        # form.fecha_expedicion.data=automotor.fecha_expedicion
        # form.avaluo.data=automotor.avaluo
        # form.seccion.data=automotor.seccion
        # form.clase_vehiculo.data=automotor.clase_vehiculo
        # form.marca.data=automotor.marca
        # form.combustible.data=automotor.combustible
        # form.modelo.data=automotor.modelo
        # form.cilindraje.data=automotor.cilindraje
        # form.color.data=automotor.color
        # form.numero_motor.data=automotor.numero_motor
        # form.numero_serie.data=automotor.numero_serie
        # form.numero_chasis.data=automotor.numero_chasis
        # form.tipo_caja.data=automotor.tipo_caja
        # form.capacidad.data=automotor.capacidad

    if form.validate_on_submit():
        inventario = inventarioVial(
            fecha_creacion=form.fecha_creacion.data,
            fecha_actualizacion=form.fecha_actualizacion.data,
            nombre=form.nombre.data,            
            descripcion=form.descripcion.data,
            codigo=form.codigo.data,
            coordenadas_inicio=form.coordenadas_inicio.data,
            coordenadas_final=form.coordenadas_final.data,
            sector=form.sector.data,
            ancho_promedio=form.ancho_promedio.data,
            longitud=form.longitud.data,
            visitador=form.visitador.data,
            pendiente_promedio=form.pendiente_promedio.data,
            tipo_de_calzada=form.tipo_de_calzada.data,
            conexion_inicio=form.conexion_inicio.data,
            conexion_final=form.conexion_final.data,
            afectada_invierno=form.afectada_invierno.data,
            requiere_mantenimiento=form.requiere_mantenimiento.data,
            estado_general=form.estado_general.data,

        )
        #Valido Formulario Formato Inventario Vial
        if form.formato.data:

            formato=request.files[form.formato.name]
            if formato.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(formato.filename)[1]
            if formato:                
                if file_ext not in FORMATO_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Formato ( xls xlsx pdf)')
                    return redirect(url_for('InventarioVial.crear_IV'))
                else:                    
                    filename = secure_filename(formato.filename)
                    inventario.filename_formato=filename
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    formato.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    inventario.path_formato=os.path.join(UPLOAD_FOLDER, filenamehash)

        #Valido Formulario Archivo SIG
        if form.archivo_sig.data:

            archivo_sig=request.files[form.archivo_sig.name]
            if archivo_sig.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(archivo_sig.filename)[1]
            if archivo_sig:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Archivo SIG ( JPG PNG PDF )')
                    return redirect(url_for('InventarioVial.crear_IV'))
                else:                    
                    filename = secure_filename(archivo_sig.filename)
                    inventario.filename_archivo_sig=filename
                    
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    archivo_sig.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    inventario.path_archivo_sig=os.path.join(UPLOAD_FOLDER, filenamehash)
        
        db.session.add(inventario)
        db.session.commit()
        flash('Registro Inventario Vial Guardado con exito') 
        return redirect(url_for('InventarioVial.crear_IV'))

    return render_template('InventarioVial/crear.html', form=form)

@bp.route('/visualizar', methods=['GET', 'POST'])
@login_required

def visualizar_IV():
    print('########################   USUARIO: ##################')
    print(current_user)
    inventario = inventarioVial.query.order_by(inventarioVial.codigo.asc())
    return render_template('InventarioVial/visualizar.html',inventario=inventario,image_name=image_names)


@bp.route('/detalles/<value>', methods=['GET', 'POST'])
@login_required

def detalles_IV(value):

    inventario=inventarioVial.query.get(value)
    
    context = {
        'inventario':inventario,

    }

    return render_template('InventarioVial/detalles.html',**context)