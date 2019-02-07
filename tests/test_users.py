"""File to test all meetup endpoints"""
import json
from base64 import b64encode
from tests.basetest import BaseTest
from requests.auth import HTTPBasicAuth as auth

user = {
	"firstname": "Test",
	"lastname": "User",
	"email": "testuser@test.com",
	"password": "Password1@"
}

class TestMeetups(BaseTest):
    """ Class to test all user endpoints """

    def test_user_signup(self):
        """Method to test user signup endpoint"""
        url = "/api/v2/auth/signup"

        response = self.post(url, user)
        result = json.loads(response.data.decode("UTF-8"))

        self.assertEqual(result["status"], 201)

    def test_user_login(self):
        """Method to test user login endpoint"""
        url = "/api/v2/auth/login"
        userAndPass = b64encode(b"test@test.com:Password1@")
        headers = { 'Authorization' : 'Basic %s' %  userAndPass }
        
        response = self.client.get(url, headers=headers)
        result = json.loads(response.data.decode("UTF-8"))

        self.assertEqual(result["status"], 200)
