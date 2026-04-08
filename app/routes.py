from flask import Blueprint, request, jsonify
from .models import User, db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/register', methods=['POST'])
def register():
    data = request.json
    new_user = User(username=data['username'], password_hash=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User created"}), 201

@auth_bp.route('/auth/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "module": "auth"}), 200
