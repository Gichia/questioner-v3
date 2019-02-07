""" Create custom error messages """
from flask import Blueprint, jsonify, make_response
from werkzeug.exceptions import BadRequest

err = Blueprint("err", __name__, url_prefix="api/v2")

@err.errorhandler(400)
def bad_request(error):
    """Error to catch not allowed method"""
    return make_response(jsonify({"error": "Please provide all required fields!", "status": 400}), 400)

@err.errorhandler(405)
def method_not_allowed(error):
    """Error to catch not allowed method"""
    return make_response(jsonify({"error": "Method not allowed!", "status": 405}), 405)

@err.errorhandler(500)
def internal_server_error(error):
    """Error to catch internal server error"""
    return make_response(jsonify({"error": "Internal error!", "status": 500}), 500)

@err.errorhandler(404)
def not_found(error):
    """Error to catch page not found"""
    return make_response(jsonify({"error": "Resource not found!", "status": 404}), 404)
