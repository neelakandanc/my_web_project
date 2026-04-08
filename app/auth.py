from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

# Mock database for demonstration
USERS = {'admin': 'password123'}

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    # Key Validator: Checks for 'username' and 'password'
    required_keys = ['username', 'password']
    if not data or not all(key in data for key in required_keys):
        return jsonify({
            "message": "Missing required keys", 
            "required": required_keys
        }), 400

    username = data.get('username')
    password = data.get('password')
    
    if username in USERS and USERS[username] == password:
        return jsonify({'message': 'Login successful', 'status': 'success'}), 200
        
    return jsonify({'message': 'Invalid credentials'}), 401
