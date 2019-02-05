from flask import Blueprint, request, jsonify, make_response

user = Blueprint('user', __name__, url_prefix="/api/v2")

@user.route("/auth/signup", methods=["POST"])
def user_signup():
    """Register new user endpoint"""

    return "Home"