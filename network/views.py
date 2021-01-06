from flask import Blueprint
from flask_restful import fields, marshal_with, reqparse
from utils.decorators import validate_token
from network.models import NetworkProvider

network_bp = Blueprint('network_bp', __name__)

parser = reqparse.RequestParser()
parser.add_argument("pin_code", type=str, help="Pin code is required", required=True)

network_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "email": fields.String,
    "address": fields.String,
    "contact": fields.Integer,
    "pin_code": fields.Integer,
    "website": fields.String,
    "type": fields.String
}


@network_bp.route("/api/get_network", methods=["POST"])
@validate_token
@marshal_with(network_fields, envelope='data')
def get_network():
    args = parser.parse_args()
    result = NetworkProvider.find_by_pin_code(args["pin_code"]).all()
    return result, 200
