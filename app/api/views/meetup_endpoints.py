from flask import Blueprint, request, jsonify, make_response
from werkzeug.exceptions import BadRequest
from app.api.models.meetups_model import MeetupsModel
from app.api.models.users_model import login_required

db = MeetupsModel()

meetup = Blueprint('meetup', __name__, url_prefix="/api/v2/meetups")

@meetup.route("", methods=["POST"])
@login_required
def post_meetup(current_user):
    """Register new user endpoint"""
    error = ""
    status = 200
    response = {}

    try:
        data = request.get_json()
        db.validate_meetup_data(data)

        topic = data["topic"]
        location = data["location"]
        happeningOn = data["happeningOn"]
        tags = data["tags"]

        # if current_user["is_admin"] is False:
        #     error = "Requires Admin Login!"
        #     status = 403
        # else:
        data = dict(
            user=current_user["user_id"],
            location=location,
            topic=topic,
            happeningOn = happeningOn,
            tags=tags  
        )
            
        meetup_id = db.post_meetup(data)
        status = 201
    except BadRequest:
        raise BadRequest()

    if error:
        response.update({"status": status, "error": error})
        return jsonify(response), status

    response.update({"status": status, "data": meetup_id})
    return jsonify(response), status
