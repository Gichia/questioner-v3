from flask import Blueprint, request, jsonify, make_response
from werkzeug.exceptions import BadRequest
from app.api.models.users_model import UsersModel

db = UsersModel()

user = Blueprint('user', __name__, url_prefix="/api/v2")

@user.route("/auth/signup", methods=["POST"])
def user_signup():
    """Register new user endpoint"""
    error = ""
    status = 200
    response = {}

    try:
        data = request.get_json()
        db.validate_signup_data(data)

        email = data["email"]
        firstname = data["firstname"]
        lastname = data["lastname"]
        password = data["password"]

        if db.is_valid_email(email) is False:
            error = "Please provide a valid email!"
            status = 400
        elif db.is_valid_password(password) is False:
            error = "Please provide a stronger password!"
            status = 400
        else:
            if db.get_email(email):
                error = "That email exists!"
                status = 409
            else:
                user_data = {
                    "firstname": firstname,
                    "lastname": lastname,
                    "email": email,
                    "password": password
                }

                db.register_user(user_data)
                status = 201
    except BadRequest:
        raise BadRequest()

    if error:
        response.update({"status": status, "error": error})
        return jsonify(response), status

    response.update({"status": status, "data": user_data})
    return jsonify(response), status

@user.route("/auth/login", methods=["GET"])
def user_login():
    """Login user endpoint"""
    error = ""
    status = 200
    token = None
    response = {}

    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        error = 'Please provide your login info'
        status = 401

    token = db.login_user(auth.username, auth.password)

    if not token:
        error = 'Incorrect login details!'
        status = 401
    else:
        status = 200

    if error:
        response.update({"status": status, "error": error})
        return jsonify(response), status

    response.update({"status": status, "data": token})
    return jsonify(response), status
