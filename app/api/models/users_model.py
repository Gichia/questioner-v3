'''Users model class'''
import datetime
from app.api.models.basemodel import BaseModel
from app.api.utils.validations import Validations
from werkzeug.exceptions import BadRequest, NotFound
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
    
    @staticmethod
    def validate_signup_data(data):
        if not all(key in data for key in ["firstname", "lastname", "email"]):
            raise BadRequest
        elif not data["firstname"].strip() or not data["lastname"].strip() \
            or not data["email"] or not data["password"]:
            raise BadRequest
        else:
            return True