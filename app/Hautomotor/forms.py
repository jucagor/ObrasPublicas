from flask import request
from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, FileField, IntegerField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import ValidationError, DataRequired, Length, Optional
from flask_babel import _, lazy_gettext as _l
from app.models import User


class CrearHVAForm(FlaskForm):
    
    placa = StringField('Placa')
    descripcion = StringField('Descripcion')
    propietario = StringField('Propietario')
    identificacion = StringField('Indentificacion interna')
    tarjeta = StringField('Numero Tarjeta Propiedad')
    fecha_expedicion = DateField('Fecha de expedicion',format='%d/%m/%Y', default=date.today)
    avaluo = IntegerField('Avaluo del automotor')
    seccion = StringField('Seccion')
    clase_vehiculo = StringField('Clase de automotor')
    marca = StringField('Marca')
    combustible = StringField('Tipo de combustible')
    modelo = StringField('Modelo')
    cilindraje = StringField('cilindraje')
    color = StringField('color')
    numero_motor = StringField('Numero de Motor')
    numero_serie = StringField('Numero de Serie')
    numero_chasis = StringField('Numero de Chasis')
    tipo_caja = StringField('Tipo de Caja')
    capacidad = StringField('Capacidad')
    #Archivos Adjuntos
    tarjeta_propiedad = FileField('Tarjeta Propiedad', validators=[Optional(),FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'pdf', 'JPG', 'JPEG', 'PNG', 'GIF', 'PDF'], 'Solo imagenes o PDF')])
    soat = FileField('Soat', validators=[Optional(),FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'pdf', 'JPG', 'JPEG', 'PNG', 'GIF', 'PDF'], 'Solo imagenes o PDF')])
    tecnomecanica = FileField('Revision Tecnomecanica', validators=[Optional(),FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'pdf', 'JPG', 'JPEG', 'PNG', 'GIF', 'PDF'], 'Solo imagenes o PDF')])
    foto1 = FileField('Foto Frontal', validators=[FileRequired(),FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'JPG', 'JPEG', 'PNG', 'GIF'], 'Por lo menos una Foto es Obligatoria')])
    foto2 =  FileField('Foto Lateral', validators=[Optional(),FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'JPG', 'JPEG', 'PNG', 'GIF'], 'Solo imagenes o PDF')])

    submit = SubmitField('Guardar')

    

