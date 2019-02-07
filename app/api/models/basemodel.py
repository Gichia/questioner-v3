"""Base model to initiate db operations"""
from psycopg2.extras import RealDictCursor
from app.database import init_connection

class BaseModel:
    """Base model to initiate db"""
    def __init__(self):
        self.db = init_connection()
        self.curr = self.db.cursor(cursor_factory=RealDictCursor)

    def get_email(self, email):
        """Method to check if email exist"""
        query = """SELECT email FROM app_users WHERE email=%s"""

        self.curr.execute(query, (email,))
        result = self.curr.fetchone()
        return result

    def get_user(self, email):
        """Method to find single user with email"""
        query = """SELECT * FROM app_users WHERE email=%s"""

        self.curr.execute(query, (email,))
        result = self.curr.fetchone()
        return result

    def delete_user(self, email):
        """Method to delete users"""
        user = self.get_user(email)
        if user:
            query = """ DELETE FROM app_users WHERE email=%s""" 

            self.curr.execute(query, (email,))
            self.curr.commit()
            return email   

    def post_data(self, query, data):
        """Method to post data to db"""
        self.curr.execute(query, data)
        self.db.commit()
        return data
        
    def get_data(self, query):
        """Method to get data from db"""
        self.curr.execute(query)
        result = self.curr.fetchall()
        return result

    def delete_data(self, query, meetup_id):
        """Method to delete data from db"""
        self.curr.execute(query, meetup_id)
        self.db.commit()
        return True
