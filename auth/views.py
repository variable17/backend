from flask import request, g, Blueprint
from utils.decorators import validate_token

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route("/api/user/login", methods=["POST"])
@validate_token
def login():
    return {"user_name": g.user.name}
