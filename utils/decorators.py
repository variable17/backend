from flask import request, g, abort
from google.oauth2 import id_token
from google.auth.transport import requests
from auth.models import User

CLIENT_ID = "95567586964-s70ovl5v4i8vdlss5m37ltd8t5hnqov3.apps.googleusercontent.com"


def validate_token(func):
    def wrapper(*args, **kwargs):
        try:
            token = request.headers.environ['HTTP_AUTHORIZATION']
            try:
                # validate token with google
                idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
                google_id = idinfo["sub"]
                name = idinfo["name"]
                email = idinfo["email"]
                picture = idinfo["picture"]

                if not User.exist(email):
                    g.user = User.create(name, email, picture, google_id)
                else:
                    g.user = User.exist(email)
            except ValueError:
                abort(401, {"message": "Invalid token"})
        except:
            abort(401, {"message": "Invalid token"})
        return func(*args, **kwargs)
    return wrapper
