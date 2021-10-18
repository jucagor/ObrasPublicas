
#from typing import Optional
from flask_wtf import FlaskForm
from datetime import date
from wtforms import StringField, SubmitField, TextAreaField, DateField, FileField
from wtforms.validators import ValidationError, DataRequired, Length, Optional


class CrearPQRForm(FlaskForm):
    
    numero_pqr = StringField('Numero de PQR', validators=[DataRequired()])
    fecha_recibido = DateField('Fecha de recibido', format='%d/%m/%Y', default=date.today)
    descripcion = StringField('Descripcion')
    peticionario = StringField('Peticionario')
    fecha_respuesta = DateField('Fecha de respuesta', format='%d/%m/%Y', validators=[Optional()])
    respuesta = FileField('Respuesta', validators=[Optional()])
    submit = SubmitField('Guardar')