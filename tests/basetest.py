"""Base Class for our tests"""
import jwt
import json
import psycopg2
import unittest
import datetime
from app import create_app
from config import Config
from psycopg2.extras import RealDictCursor
from app.database import init_connection

user = {
	"firstname": "Test",
	"lastname": "User",
	"email": "test@test.com",
	"password": "Password1@"
}

class BaseTest(unittest.TestCase):
    """Initializes our setUp for tests"""
    def setUp(self):
        """Initializes our app and tests"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.db = init_connection()
        self.curr = self.db.cursor(cursor_factory=RealDictCursor) 

        self.client.post("/api/v2/auth/signup", data=json.dumps(user),\
            content_type="application/json")

    def post(self, url, data):
        """Method for post tests"""
        und_token = jwt.encode({'sub': "test@test.com", "exp": datetime.datetime.utcnow()\
            + datetime.timedelta(minutes=30)}, Config.SECRET_KEY)
        token = und_token.decode("UTF-8")
        headers = {"x-access-token": token}
        return self.client.post(url, data=json.dumps(data), content_type="application/json", headers=headers)

    def get_items(self, url):
        """Method for get tests"""
        return self.client.get(url)

    def tearDown(self):
        """Tear down the app after running tests"""
        query = """DELETE FROM app_users WHERE email='test@test.com'"""
        query2 = """DELETE FROM app_users WHERE email='testuser@test.com'"""
        self.curr.execute(query)
        self.curr.execute(query2)
        self.db.commit()
        self.curr.close()
        self.db.close()
