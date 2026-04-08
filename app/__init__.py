import os
from flask import Flask
from .auth import auth_bp
from .catalog import catalog_bp
from .orders import orders_bp
from .profile import profile_bp
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for 
def create_app():
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
    
    app = Flask(__name__, template_folder=template_dir)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(catalog_bp, url_prefix='/catalog')
    app.register_blueprint(orders_bp, url_prefix='/orders')
    app.register_blueprint(profile_bp, url_prefix='/profile')

    @app.route('/')
    def home():
        # Check for a 'user_session' cookie
        user = request.cookies.get('user_session')
        if not user:
            # If no cookie, force them to the login UI
            return redirect(url_for('auth.login_page'))
        return render_template('index.html', username=user)
        
    return app
