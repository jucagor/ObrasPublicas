from flask import request
from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, FileField
from wtforms.validators import ValidationError, DataRequired, Length, Optional
from flask_babel import _, lazy_gettext as _l
from app.models import User


class CrearHVOForm(FlaskForm):
    
    nombre = StringField('Nombre de la Obra')
    descripcion = StringField('Descripcion')
    direccion = StringField('Direccion')
    radicado = StringField('Radicado de solicitud')
    ingeniero = StringField('Ingeniero a cargo')
    localizacion = StringField('Localizacion')
    estado = StringField('Estado de la obra')
    fecha_inicio = DateField('Fecha de inicio de la obra',format='%d/%m/%Y', default=date.today)
    terminacion = DateField('Fecha de terminacion de la obra', format='%d/%m/%Y')
    fecha_socializacion = DateField('Fecha de socializacion', format='%d/%m/%Y', default=date.today)

    file_base_datos = FileField('Cuadro base de Datos', validators=[Optional()])
    programa_visitas = FileField('Porgrama de visitas', validators=[Optional()])
    visita_tecnica = FileField('Visita Tecnica', validators=[Optional()])
    acta_comite_tecnico = FileField('Acta de comite Tecnico', validators=[Optional()])
    certificado_banco_proyectos =  FileField('Certificado Banco de proyectos', validators=[Optional()])
    presupuesto_obra = FileField('Presupuesto de Obra', validators=[Optional()])
    estudios_previos = FileField('Estudios previos y Certificado de disponibilidad presupuestal', validators=[Optional()])
    estado_redes =  FileField('Estado de Redes', validators=[Optional()])
    planos = FileField('Planos', validators=[Optional()])
    ensayo_laboratorio = FileField('Ensayo de laboratorio', validators=[Optional()])
    plan_ambiental = FileField('Plan de manejo ambiental', validators=[Optional()])
    registro_fotografico = FileField('Registro fotografico', validators=[Optional()])
    formato_informe_diario = FileField('Formato de registro de informe diario', validators=[Optional()])
    acta_entrega = FileField('Acta de entrega de la Obra', validators=[Optional()])
    consolidacion_documentos = FileField('Consolidacion documentos hoja de vida', validators=[Optional()])
    submit = SubmitField('Guardar')

    

