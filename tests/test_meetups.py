import json
from tests.basetest import BaseTest

meetup = {
	"topic": "Petetr",
	"location": "Gichia",
	"happeningOn": "peter@test.com",
	"tags": ["Web Design"]
}

class MeetupsTest(BaseTest):
    '''Class to add all meetup tests'''

    def test_post_meetup(self):
        url = "/api/v2/meetups"

        response = self.post(url, meetup)
        result = json.loads(response.data.decode("UTF-8"))

        self.assertEqual(result["status"], 201)
