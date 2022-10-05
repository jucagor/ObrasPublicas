from flask import render_template, redirect, url_for, flash, request, send_from_directory
from flask_login import current_user, login_required
from app import db
from app.HVObra import bp
#from app.auth.forms import LoginForm, RegistrationForm
from app.models import Hojaobra
from app.HVObra.forms import CrearHVOForm
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from hashlib import md5
# from app.auth.email import send_password_reset_email


UPLOAD_FOLDER = '/home/camilo/projects/alcaldia/Files/HojaObra'
IMAGES_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.pdf', '.JPG', '.JPEG', '.PNG', '.GIF', '.PDF']

def recepcion_formulario(formulario,hv):
    print("Procesando formulario de:",formulario.name)
    if formulario.data:
        data=request.files[formulario.name]
        if data.filename=='':
            flash('No selecciono ningun archivo')
            return redirect(request.url)

        file_ext = os.path.splitext(data.filename)[1]
        if data:                
            if file_ext not in IMAGES_EXTENSIONS:
                flash('Selecciona un archivo Valido ( JPG PNG GIF PDF )')
                return redirect(url_for('HVObra.crear_HVO'))
            else:                    
                filename = secure_filename(data.filename)
                #hv.filename_cuadro_base_datos=filename                      #####SOLUCIONAR!!!!!####
                exec("hv.filename_"+ formulario.name + "=filename")
                filename, file_extension = os.path.splitext(filename)
                filenamehash = str(datetime.now())+filename
                filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                data.save(os.path.join(UPLOAD_FOLDER, filenamehash))                
                #hv.path_cuadro_base_datos=os.path.join(UPLOAD_FOLDER, filenamehash)     #####SOLUCIONAR!!!!!####
                exec("hv.path_"+ formulario.name + "=os.path.join(UPLOAD_FOLDER, filenamehash)")

@bp.route('/crear', methods=['GET', 'POST'])
@login_required

def crear_HVO():
    form = CrearHVOForm()
    id_hojaobra = request.args.get('id',None)
    if id_hojaobra is not None:
        #Consulto la Hoja de vida en la base de datos
        hojaobra=Hojaobra.query.filter_by(id=id_hojaobra).first()

    if form.validate_on_submit():
        hv = Hojaobra(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            direccion=form.direccion.data,
            radicado_solicitud=form.radicado.data,
            ingeniero_a_cargo=form.ingeniero.data,
            localizacion=form.localizacion.data,
            estado=form.estado.data,
            fecha_inicio=form.fecha_inicio.data,
            fecha_terminacion=form.terminacion.data,
            fecha_socializacion=form.fecha_socializacion.data,
        )

        #Valido Formulario para base de datos

        if form.cuadro_base_datos.data:
            recepcion_formulario(form.cuadro_base_datos,hv)

        #Valido Formulario Tarjeta de Propiedad
        if form.programa_visitas.data:
            recepcion_formulario(form.programa_visitas,hv)

        #Valido Formulario Tarjeta de Propiedad
        if form.visita_tecnica.data:
            recepcion_formulario(form.visita_tecnica,hv)
        
        #Valido Formulario Tarjeta de Propiedad
        if form.acta_comite_tecnico.data:
            recepcion_formulario(form.acta_comite_tecnico,hv)

        #Valido Formulario Tarjeta de Propiedad
        if form.certificado_banco_proyectos.data:
            recepcion_formulario(form.certificado_banco_proyectos,hv)

        #Valido Formulario Tarjeta de Propiedad
        if form.presupuesto.data:
            recepcion_formulario(form.presupuesto,hv)

        #Valido Formulario Tarjeta de Propiedad
        if form.estudios_previos.data:
            recepcion_formulario(form.estudios_previos,hv)

        #Valido Formulario Tarjeta de Propiedad
        if form.estado_redes.data:
            recepcion_formulario(form.estado_redes,hv)

        #Valido Formulario Tarjeta de Propiedad
        if form.planos.data:
            recepcion_formulario(form.planos,hv)

        #Valido Formulario Tarjeta de Propiedad
        if form.ensayo_laboratorio.data:
            recepcion_formulario(form.ensayo_laboratorio,hv)

        #Valido Formulario Tarjeta de Propiedad
        if form.plan_manejo_ambiental.data:
            recepcion_formulario(form.plan_manejo_ambiental,hv)

        #Valido Formulario Tarjeta de Propiedad
        if form.registro_fotografico.data:
            recepcion_formulario(form.registro_fotografico,hv)

        #Valido Formulario Tarjeta de Propiedad
        if form.informe_diario.data:
            recepcion_formulario(form.informe_diario,hv)

        #Valido Formulario Tarjeta de Propiedad
        if form.acta_de_entrega.data:
            recepcion_formulario(form.acta_de_entrega,hv)

        #Valido Formulario Tarjeta de Propiedad
        if form.consolidacion_documentos.data:
            recepcion_formulario(form.consolidacion_documentos,hv)        

        db.session.add(hv)
        db.session.commit()
        flash('Hoja de vida de Obra Guardada con exito')  
        return redirect(url_for('HVObra.crear_HVO'))

    return render_template('HVObra/crear.html', form=form)

@bp.route('/visualizar', methods=['GET', 'POST'])
@login_required

def visualizar_HVO():
    hojas_de_vida = Hojaobra.query.order_by(Hojaobra.fecha_ultima_actualizacion.asc())
    return render_template('HVObra/visualizar.html',hojas_vida=hojas_de_vida)

##########################################################

@bp.route('/detalles/<value>', methods=['GET', 'POST'])
@login_required

def detalles_HVO(value):

    hv=Hojaobra.query.get(value)
    
    context = {
        'hv':hv,

    }

    if request.method == 'POST':
        archivo=request.form.get('archivo')
        print(archivo)

        if archivo=="cuadro_base_datos":

            if hv.path_cuadro_base_datos!=None:
                return send_from_directory(UPLOAD_FOLDER,hv.path_cuadro_base_datos.split('/')[7],as_attachment=True)
            else:
                flash("No existe este documento!!")

        elif archivo=="programa_visitas":
            if hv.path_programa_visitas!=None:
                return send_from_directory(UPLOAD_FOLDER,hv.path_programa_visitas.split('/')[7],as_attachment=True)
            else:
                flash("No existe este documento!!")

        elif archivo=="visita_tecnica":
            if hv.path_visita_tecnica!=None:
                return send_from_directory(UPLOAD_FOLDER,hv.path_visita_tecnica.split('/')[7],as_attachment=True)
            else:
                flash("No existe este documento!!")

        elif archivo=="acta_comite_tecnico":
            if hv.path_acta_comite_tecnico!=None:
                return send_from_directory(UPLOAD_FOLDER,hv.path_acta_comite_tecnico.split('/')[7],as_attachment=True)
            else:
                flash("No existe este documento!!")

        elif archivo=="certificado_banco_proyectos":
            return send_from_directory(UPLOAD_FOLDER,hv.path_certificado_banco_proyectos.split('/')[7],as_attachment=True)

        elif archivo=="presupuesto":
            return send_from_directory(UPLOAD_FOLDER,hv.path_presupuesto.split('/')[7],as_attachment=True)

        elif archivo=="estudios_previos":
            return send_from_directory(UPLOAD_FOLDER,hv.path_estudios_previos.split('/')[7],as_attachment=True)

        elif archivo=="estado_redes":
            return send_from_directory(UPLOAD_FOLDER,hv.path_estado_redes.split('/')[7],as_attachment=True)
        
        elif archivo=="planos":
            return send_from_directory(UPLOAD_FOLDER,hv.path_planos.split('/')[7],as_attachment=True)
        
        elif archivo=="ensayo_laboratorio":
            return send_from_directory(UPLOAD_FOLDER,hv.path_ensayo_laboratorio.split('/')[7],as_attachment=True)
        
        elif archivo=="plan_manejo_ambiental":
            return send_from_directory(UPLOAD_FOLDER,hv.path_plan_manejo_ambiental.split('/')[7],as_attachment=True)

        elif archivo=="registro_fotografico":
            return send_from_directory(UPLOAD_FOLDER,hv.path_registro_fotografico.split('/')[7],as_attachment=True)
        
        elif archivo=="informe_diario":
            return send_from_directory(UPLOAD_FOLDER,hv.path_informe_diario.split('/')[7],as_attachment=True)
        
        elif archivo=="acta_de_entrega":
            return send_from_directory(UPLOAD_FOLDER,hv.path_acta_de_entrega.split('/')[7],as_attachment=True)
        
        elif archivo=="consolidacion_documentos":
            return send_from_directory(UPLOAD_FOLDER,hv.path_consolidacion_documentos.split('/')[7],as_attachment=True)

    return render_template('HVObra/detalles.html',**context)