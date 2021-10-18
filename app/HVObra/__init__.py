from flask import Blueprint

bp = Blueprint('HVObra', __name__)

from app.HVObra import routes
