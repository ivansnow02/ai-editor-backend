from . import main
from flask import jsonify

@main.app_errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "404 Not Found"}), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return  jsonify({"error": "500 Internal Server Error"}), 500