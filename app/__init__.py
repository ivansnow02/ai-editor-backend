from flask import Flask
from config import config
from flask_cors import CORS


def create_app(config_name) -> Flask:
    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    

    return app
