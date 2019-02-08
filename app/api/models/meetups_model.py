import datetime
from werkzeug.exceptions import BadRequest
from app.api.models.basemodel import BaseModel
from app.api.utils.validations import Validations

class MeetupsModel(BaseModel, Validations):
    '''Meetup model for all meetup operations'''

    def post_meetup(self, data):
        """Method to post a new meetup"""
        meetup = {
            "created_by": data["user"],
            "location": data["location"],
            "topic": data["topic"],
            "tags": data["tags"],
            "createdon": datetime.datetime.now()
        }

        query = """INSERT INTO meetups (created_by, location, topic, tags, createdon)\
                VALUES ( %(created_by)s, %(location)s, %(topic)s, %(tags)s, %(createdon)s )\
                RETURNING meetup_id"""

        meetup_id = self.post_data(query, meetup)
        return meetup_id

    @staticmethod
    def validate_meetup_data(data):
        if not all(key in data for key in ["topic", "location", "happeningOn"]):
            raise BadRequest
        elif not data["topic"].strip() or not data["location"].strip()\
            or not data["happeningOn"]:
            raise BadRequest
        else:
            return True