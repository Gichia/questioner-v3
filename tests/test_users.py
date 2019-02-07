"""File to test all meetup endpoints"""
import os
import psycopg2 as pg2
import json
from tests.basetest import BaseTest

user = {
	"firstname": "Test",
	"lastname": "User",
	"email": "testuser@test.com",
	"password": "Password1@"
}

class TestMeetups(BaseTest):
    """ Class to test all user endpoints """

    def test_user_signup(self):
        """Method to test post meetup endpoint"""
        url = "/api/v2/auth/signup"

        response = self.post(url, user)
        result = json.loads(response.data.decode("UTF-8"))

        self.assertEqual(result["status"], 201)
