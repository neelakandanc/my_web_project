import os
from flask import Flask
from .auth import auth_bp
from .catalog import catalog_bp
from .orders import orders_bp
from .profile import profile_bp
from flask import render_template

def create_app():
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
    
    app = Flask(__name__, template_folder=template_dir)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(catalog_bp, url_prefix='/catalog')
    app.register_blueprint(orders_bp, url_prefix='/orders')
    app.register_blueprint(profile_bp, url_prefix='/profile')

    @app.route('/')
    def home():
        return render_template('index.html')
        
    return app
