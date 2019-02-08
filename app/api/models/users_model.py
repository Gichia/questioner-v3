'''Users model class'''
import jwt
import datetime
from config import Config
from functools import wraps
from flask import request, jsonify, make_response
from werkzeug.exceptions import BadRequest, NotFound
from app.api.models.basemodel import BaseModel
from app.api.utils.validations import Validations
from werkzeug.security import generate_password_hash, check_password_hash

class UsersModel(BaseModel, Validations):
    '''User model for all user operations'''

    def register_user(self, data):
        """Method to add new user to db""" 
        new_user = dict(
            firstname = data["firstname"],
            lastname = data["lastname"],
            email = data["email"],
            created_on = datetime.datetime.now(),
            username = data["email"].split('@')[:1],
            phonenumber = None,
            password = generate_password_hash(data["password"])
        )
        
        query = """INSERT INTO app_users (firstname, lastname, email, created_on, username, phonenumber, \
            password) VALUES ( %(firstname)s, %(lastname)s, \
            %(email)s, %(created_on)s, %(username)s, %(phonenumber)s, %(password)s )"""

        data = self.post_data(query, new_user)
        return data

    def login_user(self, email, password):
        """Function to login user and create token"""
        user = self.get_user(email)

        if user:
            user_data = {
                "user_id": user["user_id"],
                "firstname": user["firstname"].strip(),
                "lastname": user["lastname"].strip(),
                "email": user["email"].strip(),
                "createdOn": user["created_on"].strip(),
                "isAdmin": user["is_admin"],
                "password": user["password"].strip()
            }

            if check_password_hash(user_data["password"], password):
                token = jwt.encode({"sub": user_data["email"], "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, Config.SECRET_KEY)
                return token.decode("UTF-8")
    
    @staticmethod
    def validate_signup_data(data):
        if not all(key in data for key in ["firstname", "lastname", "email"]):
            raise BadRequest
        elif not data["firstname"].strip() or not data["lastname"].strip()\
            or not data["email"] or not data["password"]:
            raise BadRequest
        else:
            return True


def login_required(f):
    """A decorated function for login required!"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]

        if not token:
            return make_response(jsonify({"status": 401, "error":"Login required!"}), 401)

        try:
            data = jwt.decode(token, Config.SECRET_KEY)
            current_user = UsersModel().get_user(data["sub"])
        except:
            return make_response(jsonify({"status": 401, "error":"Token is Invalid, Please Login Again!"}), 401)

        return f(current_user, *args, **kwargs)
    return decorated