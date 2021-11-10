from flask import request
from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, FileField, IntegerField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import ValidationError, DataRequired, Length, Optional
from flask_babel import _, lazy_gettext as _l
from app.models import User


class CrearIVForm(FlaskForm):
    
    fecha_creacion = DateField('Fecha de Creacion',format='%d/%m/%Y', default=date.today)
    fecha_actualizacion = DateField('Fecha de ultima actualizacion',format='%d/%m/%Y', default=date.today)
    nombre = StringField('Nombre de la via')
    descripcion = StringField('Descripcion')
    codigo = StringField('Codigo de la via')
    coordenadas_inicio = StringField('Coordenada inicial')
    coordenadas_final = StringField('Coordenada Final')
    sector = StringField('Sector')
    ancho_promedio = StringField('Ancho promedio')
    longitud = StringField('Longitud de la via')
    visitador = StringField('Visitador')
    pendiente_promedio = StringField('Pendiente promedio')
    tipo_de_calzada = StringField('Tipo de Calzada')
    conexion_inicio = StringField('Conecta al final con')
    conexion_final = StringField('Conecta al final con:')
    afectada_invierno = StringField('Via se puede ver afectada por invierno')
    requiere_mantenimiento = StringField('Via Requiere mantenimiento?')
    estado_general = StringField('Estado general de la via')
    #Archivos Adjuntos
    formato = FileField('Formato de Inventario Vial', validators=[Optional(),FileAllowed(['xls', 'xlsx', 'pdf', 'XLS', 'XLSX' 'PDF'], 'Solo archivos excel o PDF')])
    archivo_sig = FileField('Archivo SIG de la via', validators=[Optional(),])

    submit = SubmitField('Guardar')

    

