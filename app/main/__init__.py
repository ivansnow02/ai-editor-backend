from flask import Blueprint

main = Blueprint("main", __name__, url_prefix="/api")

from . import views, errors
