from flask import Blueprint

bp = Blueprint('PQRS', __name__)

from app.PQRS import routes
