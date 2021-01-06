from flask import g, Blueprint
from flask_restful import fields, marshal_with
from utils.decorators import validate_token

auth_bp = Blueprint('auth_bp', __name__)

user_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "email": fields.String,
    "picture": fields.String
}


@auth_bp.route("/api/user/login", methods=["POST"])
@validate_token
@marshal_with(user_fields)
def login():
    return g.user, 200
