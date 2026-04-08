from flask import Blueprint, request, jsonify

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/update-bio', methods=['PUT'])
def update_bio():
    """AI Target: User Metadata Updates"""
    return jsonify({"status": "bio updated"}), 200

@profile_bp.route('/settings', methods=['PATCH'])
def update_settings():
    """AI Target: Privacy & Notification Logic"""
    return jsonify({"notifications": "enabled"}), 200

@profile_bp.route('/avatar', methods=['POST'])
def upload_avatar():
    """AI Target: Static Asset Handling"""
    return jsonify({"url": "/uploads/avatar_1.png"}), 200
