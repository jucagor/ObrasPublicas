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
        if form.file_base_datos.data:
            file_base_datos=request.files[form.file_base_datos.name]
            if file_base_datos.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(file_base_datos.filename)[1]
            if file_base_datos:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Tarjeta de Propiedad ( JPG PNG GIF PDF )')
                    return redirect(url_for('Hautomotor.crear_HVA'))
                else:                    
                    filename = secure_filename(file_base_datos.filename)
                    hv.filename_cuadro_base_datos=filename
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    file_base_datos.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    hv.path_cuadro_base_datos=os.path.join(UPLOAD_FOLDER, filenamehash)

        #Valido Formulario Tarjeta de Propiedad
        if form.programa_visitas.data:

            programa_visitas=request.files[form.programa_visitas.name]
            if programa_visitas.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(programa_visitas.filename)[1]
            if programa_visitas:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Tarjeta de Propiedad ( JPG PNG GIF PDF )')
                    return redirect(url_for('Hautomotor.crear_HVA'))
                else:                    
                    filename = secure_filename(programa_visitas.filename)
                    hv.filename_programa_visitas=filename
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    programa_visitas.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    hv.path_programa_visitas=os.path.join(UPLOAD_FOLDER, filenamehash)

        #Valido Formulario Tarjeta de Propiedad
        if form.visita_tecnica.data:

            visita_tecnica=request.files[form.visita_tecnica.name]
            if visita_tecnica.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(visita_tecnica.filename)[1]
            if visita_tecnica:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Tarjeta de Propiedad ( JPG PNG GIF PDF )')
                    return redirect(url_for('Hautomotor.crear_HVA'))
                else:                    
                    filename = secure_filename(visita_tecnica.filename)
                    hv.filename_visita_tecnica=filename
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    visita_tecnica.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    hv.path_visita_tecnica=os.path.join(UPLOAD_FOLDER, filenamehash)
        
        #Valido Formulario Tarjeta de Propiedad
        if form.acta_comite_tecnico.data:

            acta_comite_tecnico=request.files[form.acta_comite_tecnico.name]
            if acta_comite_tecnico.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(acta_comite_tecnico.filename)[1]
            if acta_comite_tecnico:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Tarjeta de Propiedad ( JPG PNG GIF PDF )')
                    return redirect(url_for('Hautomotor.crear_HVA'))
                else:                    
                    filename = secure_filename(acta_comite_tecnico.filename)
                    hv.filename_acta_comite_tecnico=filename
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    acta_comite_tecnico.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    hv.path_acta_comite_tecnico=os.path.join(UPLOAD_FOLDER, filenamehash)

        #Valido Formulario Tarjeta de Propiedad
        if form.certificado_banco_proyectos.data:

            certificado_banco_proyectos=request.files[form.certificado_banco_proyectos.name]
            if certificado_banco_proyectos.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(certificado_banco_proyectos.filename)[1]
            if certificado_banco_proyectos:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Tarjeta de Propiedad ( JPG PNG GIF PDF )')
                    return redirect(url_for('Hautomotor.crear_HVA'))
                else:                    
                    filename = secure_filename(certificado_banco_proyectos.filename)
                    hv.filename_certificado_banco_proyectos=filename
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    certificado_banco_proyectos.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    hv.path_certificado_banco_proyectos=os.path.join(UPLOAD_FOLDER, filenamehash)

        #Valido Formulario Tarjeta de Propiedad
        if form.presupuesto_obra.data:

            presupuesto_obra=request.files[form.presupuesto_obra.name]
            if presupuesto_obra.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(presupuesto_obra.filename)[1]
            if presupuesto_obra:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Tarjeta de Propiedad ( JPG PNG GIF PDF )')
                    return redirect(url_for('Hautomotor.crear_HVA'))
                else:                    
                    filename = secure_filename(presupuesto_obra.filename)
                    hv.filename_presupuesto_obra=filename
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    presupuesto_obra.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    hv.path_presupuesto_obra=os.path.join(UPLOAD_FOLDER, filenamehash)

        #Valido Formulario Tarjeta de Propiedad
        if form.estudios_previos.data:

            estudios_previos=request.files[form.estudios_previos.name]
            if estudios_previos.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(estudios_previos.filename)[1]
            if estudios_previos:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Tarjeta de Propiedad ( JPG PNG GIF PDF )')
                    return redirect(url_for('Hautomotor.crear_HVA'))
                else:                    
                    filename = secure_filename(estudios_previos.filename)
                    hv.filename_estudios_previos=filename
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    estudios_previos.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    hv.path_estudios_previos=os.path.join(UPLOAD_FOLDER, filenamehash)

        #Valido Formulario Tarjeta de Propiedad
        if form.estado_redes.data:

            estado_redes=request.files[form.estado_redes.name]
            if estado_redes.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(estado_redes.filename)[1]
            if estado_redes:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Tarjeta de Propiedad ( JPG PNG GIF PDF )')
                    return redirect(url_for('Hautomotor.crear_HVA'))
                else:                    
                    filename = secure_filename(estado_redes.filename)
                    hv.filename_estado_redes=filename
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    estado_redes.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    hv.path_estado_redes=os.path.join(UPLOAD_FOLDER, filenamehash)

        #Valido Formulario Tarjeta de Propiedad
        if form.planos.data:

            planos=request.files[form.planos.name]
            if planos.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(planos.filename)[1]
            if planos:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Tarjeta de Propiedad ( JPG PNG GIF PDF )')
                    return redirect(url_for('Hautomotor.crear_HVA'))
                else:                    
                    filename = secure_filename(planos.filename)
                    hv.filename_planos=filename
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    planos.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    hv.path_planos=os.path.join(UPLOAD_FOLDER, filenamehash)

        #Valido Formulario Tarjeta de Propiedad
        if form.ensayo_laboratorio.data:

            ensayo_laboratorio=request.files[form.ensayo_laboratorio.name]
            if ensayo_laboratorio.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(ensayo_laboratorio.filename)[1]
            if ensayo_laboratorio:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Tarjeta de Propiedad ( JPG PNG GIF PDF )')
                    return redirect(url_for('Hautomotor.crear_HVA'))
                else:                    
                    filename = secure_filename(ensayo_laboratorio.filename)
                    hv.filename_ensayo_laboratorio=filename
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    ensayo_laboratorio.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    hv.path_ensayo_laboratorio=os.path.join(UPLOAD_FOLDER, filenamehash)

        #Valido Formulario Tarjeta de Propiedad
        if form.plan_ambiental.data:

            plan_ambiental=request.files[form.plan_ambiental.name]
            if plan_ambiental.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(plan_ambiental.filename)[1]
            if plan_ambiental:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Tarjeta de Propiedad ( JPG PNG GIF PDF )')
                    return redirect(url_for('Hautomotor.crear_HVA'))
                else:                    
                    filename = secure_filename(plan_ambiental.filename)
                    hv.filename_plan_ambiental=filename
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    plan_ambiental.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    hv.path_plan_ambiental=os.path.join(UPLOAD_FOLDER, filenamehash)

        #Valido Formulario Tarjeta de Propiedad
        if form.registro_fotografico.data:

            registro_fotografico=request.files[form.registro_fotografico.name]
            if registro_fotografico.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(registro_fotografico.filename)[1]
            if registro_fotografico:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Tarjeta de Propiedad ( JPG PNG GIF PDF )')
                    return redirect(url_for('Hautomotor.crear_HVA'))
                else:                    
                    filename = secure_filename(registro_fotografico.filename)
                    hv.filename_registro_fotografico=filename
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    registro_fotografico.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    hv.path_registro_fotografico=os.path.join(UPLOAD_FOLDER, filenamehash)

        #Valido Formulario Tarjeta de Propiedad
        if form.formato_informe_diario.data:

            formato_informe_diario=request.files[form.formato_informe_diario.name]
            if formato_informe_diario.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(formato_informe_diario.filename)[1]
            if formato_informe_diario:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Tarjeta de Propiedad ( JPG PNG GIF PDF )')
                    return redirect(url_for('Hautomotor.crear_HVA'))
                else:                    
                    filename = secure_filename(formato_informe_diario.filename)
                    hv.filename_formato_informe_diario=filename
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    formato_informe_diario.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    hv.path_formato_informe_diario=os.path.join(UPLOAD_FOLDER, filenamehash)

        #Valido Formulario Tarjeta de Propiedad
        if form.acta_entrega.data:

            acta_entrega=request.files[form.acta_entrega.name]
            if acta_entrega.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(acta_entrega.filename)[1]
            if acta_entrega:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Tarjeta de Propiedad ( JPG PNG GIF PDF )')
                    return redirect(url_for('Hautomotor.crear_HVA'))
                else:                    
                    filename = secure_filename(acta_entrega.filename)
                    hv.filename_acta_entrega=filename
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    acta_entrega.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    hv.path_acta_entrega=os.path.join(UPLOAD_FOLDER, filenamehash)

        #Valido Formulario Tarjeta de Propiedad
        if form.consolidacion_documentos.data:

            consolidacion_documentos=request.files[form.consolidacion_documentos.name]
            if consolidacion_documentos.filename == '':
                flash('No selecciono ningun archivo')
                return redirect(request.url)

            file_ext = os.path.splitext(consolidacion_documentos.filename)[1]
            if consolidacion_documentos:                
                if file_ext not in IMAGES_EXTENSIONS:
                    flash('Selecciona un archivo Valido para Tarjeta de Propiedad ( JPG PNG GIF PDF )')
                    return redirect(url_for('Hautomotor.crear_HVA'))
                else:                    
                    filename = secure_filename(consolidacion_documentos.filename)
                    hv.filename_consolidacion_documentos=filename
                    filename, file_extension = os.path.splitext(filename)
                    filenamehash = str(datetime.now())+filename
                    filenamehash = md5(filenamehash.encode('utf-8')).hexdigest()+file_extension
                    consolidacion_documentos.save(os.path.join(UPLOAD_FOLDER, filenamehash))
                    hv.path_consolidacion_documentos=os.path.join(UPLOAD_FOLDER, filenamehash)


        

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
                return send_from_directory(UPLOAD_FOLDER,hv.path_acta_comite_tecnico.split.split('/')[7],as_attachment=True)
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