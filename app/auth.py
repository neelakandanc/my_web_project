from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

# Mock database for demonstration
USERS = {'admin': 'password123'}

@auth_bp.route('/login', methods=['POST'])
def login():
    """Endpoint for user authentication."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username in USERS and USERS[username] == password:
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401
