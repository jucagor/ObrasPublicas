import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from elasticsearch import Elasticsearch
from redis import Redis
import rq
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = ('Porfavor inicie sesion para acceder a esta pagina')
mail = Mail()
bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    #moment.init_app(app)
    #babel.init_app(app)
    #app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
    #   if app.config['ELASTICSEARCH_URL'] else None
    #app.redis = Redis.from_url(app.config['REDIS_URL'])
    #app.task_queue = rq.Queue('microblog-tasks', connection=app.redis)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.PQRS import bp as pqrs_bp
    app.register_blueprint(pqrs_bp, url_prefix='/PQRS')

    from app.HVObra import bp as HVObra_bp
    app.register_blueprint(HVObra_bp, url_prefix='/HojaDeVidaObras')

    from app.Hautomotor import bp as Hautomotor_bp
    app.register_blueprint(Hautomotor_bp, url_prefix='/HojaDeVidaAutomotor')

    from app.InventarioVial import bp as InventarioVial_bp
    app.register_blueprint(InventarioVial_bp, url_prefix='/InventarioVial')


    return app

#@babel.localeselector
#def get_locale():
#    return request.accept_languages.best_match(current_app.config['LANGUAGES'])


from app import models
