import base64
from datetime import datetime, timedelta
from hashlib import md5
import json
import os
from time import time
from flask import current_app, url_for
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
# import jwt
# import redis
# import rq
from app import db, login
# from app.search import add_to_index, remove_from_index, query_index


# db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
# db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)


# class PaginatedAPIMixin(object):
#     @staticmethod
#     def to_collection_dict(query, page, per_page, endpoint, **kwargs):
#         resources = query.paginate(page, per_page, False)
#         data = {
#             'items': [item.to_dict() for item in resources.items],
#             '_meta': {
#                 'page': page,
#                 'per_page': per_page,
#                 'total_pages': resources.pages,
#                 'total_items': resources.total
#             },
#             '_links': {
#                 'self': url_for(endpoint, page=page, per_page=per_page,
#                                 **kwargs),
#                 'next': url_for(endpoint, page=page + 1, per_page=per_page,
#                                 **kwargs) if resources.has_next else None,
#                 'prev': url_for(endpoint, page=page - 1, per_page=per_page,
#                                 **kwargs) if resources.has_prev else None
#             }
#         }
#         return data


followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    #posts = db.relationship('Post', backref='author', lazy='dynamic')
    #about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    #token = db.Column(db.String(32), index=True, unique=True)
    # #token_expiration = db.Column(db.DateTime)
    # followed = db.relationship(
    #     'User', secondary=followers,
    #     primaryjoin=(followers.c.follower_id == id),
    #     secondaryjoin=(followers.c.followed_id == id),
    #     backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
    # messages_sent = db.relationship('Message',
    #                                 foreign_keys='Message.sender_id',
    #                                 backref='author', lazy='dynamic')
    # messages_received = db.relationship('Message',
    #                                     foreign_keys='Message.recipient_id',
    #                                     backref='recipient', lazy='dynamic')
    # last_message_read_time = db.Column(db.DateTime)
    # notifications = db.relationship('Notification', backref='user',
    #                                 lazy='dynamic')
    # tasks = db.relationship('Task', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # def avatar(self, size):
    #     digest = md5(self.email.lower().encode('utf-8')).hexdigest()
    #     return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
    #         digest, size)

  


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Hojaobra(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(240)) 
    fecha_ultima_actualizacion = db.Column(db.DateTime, default=datetime.utcnow)
    localizacion = db.Column(db.String(30))
    direccion = db.Column(db.String(40))
    radicado_solicitud = db.Column(db.String(30))
    ingeniero_a_cargo = db.Column(db.String(30))
    estado = db.Column(db.String(30))
    fecha_socializacion = db.Column(db.DateTime)
    fecha_inicio = db.Column(db.DateTime)
    fecha_terminacion = db.Column(db.DateTime)
    #   Archivos adjuntos
    path_cuadro_base_datos = db.Column(db.String(30))
    path_programa_visitas = db.Column(db.String(30))
    path_visita_tecnica = db.Column(db.String(30))
    path_acta_comite_tecnico = db.Column(db.String(30))
    path_certificado_banco_proyectos = db.Column(db.String(30))
    path_presupuesto = db.Column(db.String(30))
    path_estudios_previos = db.Column(db.String(30))
    path_estado_redes = db.Column(db.String(30))
    path_planos = db.Column(db.String(30))
    path_ensayo_laboratorio = db.Column(db.String(30))
    path_plan_manejo_ambiental = db.Column(db.String(30))
    path_registro_fotografico = db.Column(db.String(30))
    path_informe_diario = db.Column(db.String(30))
    path_acta_de_entrega = db.Column(db.String(30))
    path_consolidacion_documentos = db.Column(db.String(30))

    # PQRS asociadas

    # PQRS = db.relationship('PQR', backref='tiene', lazy='dynamic')


class PQR(db.Model):
    # __searchable__ = ['descripcion']    
    id = db.Column(db.Integer, primary_key=True, unique=True)
    fecha_recibido = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    descripcion = db.Column(db.String(240))    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    peticionario = db.Column(db.String(30))
    fecha_respuesta = db.Column(db.DateTime, index=True)
    path_respuesta = db.Column(db.String(30))
    filename_respuesta = db.Column(db.String(140))
    # Hoja_vida = db.Column(db.Integer, db.ForeignKey('Hojaobra.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class inventarioVial(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    fecha_creacion = db.Column(db.DateTime, index=True)
    fecha_actualizacion = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    nombre = db.Column(db.String(240)) 
    descripcion = db.Column(db.String(240)) 
    codigo = db.Column(db.Integer)
    ancho_promedio = db.Column(db.String(30))
    longitud = db.Column(db.String(30))
    visitador = db.Column(db.String(30))
    coordenadas_inicio = db.Column(db.String(30))
    coordenadas_final = db.Column(db.String(30))
    sector = db.Column(db.String(30))
    pendiente_promedio = db.Column(db.String(30))
    tipo_de_calzada = db.Column(db.String(30))
    conexion_inicio = db.Column(db.String(30))
    conexion_final = db.Column(db.String(30))
    afectada_invierno = db.column(db.String(30))
    requiere_mantenimiento = db.Column(db.String(30))
    estado_general = db.Column(db.String(30))

    #   Archivos adjuntos

    path_formato = db.Column(db.String(30))
    filename_formato = db.Column(db.String(30))
    path_sig = db.Column(db.String(30))
    filename_sig = db.Column(db.String(30))


class HojaAutomotor(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(240)) 
    fecha_ultima_actualizacion = db.Column(db.DateTime, default=datetime.utcnow)
    propietario = db.Column(db.String(30))
    identificacion_interna = db.Column(db.String(30))
    tarjeta_propiedad = db.Column(db.String(40))
    fecha_expedicion = db.Column(db.DateTime)
    fecha_creacion = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    avaluo = db.Column(db.Integer)
    seccion = db.Column(db.String(40))
    clase_vehiculo = db.Column(db.String(40))
    marca = db.Column(db.String(30))
    combustible = db.Column(db.String(30))
    modelo = db.Column(db.String(30))
    placa = db.Column(db.String(30))
    cilindraje = db.Column(db.String(30))
    color = db.Column(db.String(30))
    numero_motor = db.Column(db.String(40))
    numero_serie = db.Column(db.String(40))
    numero_chasis = db.Column(db.String(40))
    tipo_caja = db.Column(db.String(40))
    capacidad = db.Column(db.String(40))

    #   Archivos adjuntos

    path_tarjeta_propiedad = db.Column(db.String(30))
    filename_tarjeta_propiedad = db.Column(db.String(30))
    path_soat = db.Column(db.String(30))
    filename_soat = db.Column(db.String(30))
    path_tecno = db.Column(db.String(30))
    filename_tecno = db.Column(db.String(30))
    path_foto1 = db.Column(db.String(30))
    filename_foto1 = db.Column(db.String(30))
    path_foto2 = db.Column(db.String(30))
    filename_foto2 = db.Column(db.String(30))


# class Message(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

#     def __repr__(self):
#         return '<Message {}>'.format(self.body)


# class Notification(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128), index=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     timestamp = db.Column(db.Float, index=True, default=time)
#     payload_json = db.Column(db.Text)

#     def get_data(self):
#         return json.loads(str(self.payload_json))


# class Task(db.Model):
#     id = db.Column(db.String(36), primary_key=True)
#     name = db.Column(db.String(128), index=True)
#     description = db.Column(db.String(128))
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     complete = db.Column(db.Boolean, default=False)

#     def get_rq_job(self):
#         try:
#             rq_job = rq.job.Job.fetch(self.id, connection=current_app.redis)
#         except (redis.exceptions.RedisError, rq.exceptions.NoSuchJobError):
#             return None
#         return rq_job

#     def get_progress(self):
#         job = self.get_rq_job()
#         return job.meta.get('progress', 0) if job is not None else 100
