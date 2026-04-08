from flask import Flask
from .auth import auth_bp
from .catalog import catalog_bp
from .orders import orders_bp
from .profile import profile_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(catalog_bp, url_prefix='/catalog')
    app.register_blueprint(orders_bp, url_prefix='/orders')
    app.register_blueprint(profile_bp, url_prefix='/profile')
    return app
