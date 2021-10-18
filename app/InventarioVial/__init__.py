from flask import Blueprint

bp = Blueprint('InventarioVial', __name__)

from app.InventarioVial import routes
