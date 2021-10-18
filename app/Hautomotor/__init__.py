from flask import Blueprint

bp = Blueprint('Hautomotor', __name__)

from app.Hautomotor import routes
