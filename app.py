from flask import Flask
import config
from extensions import db, cors, api

from auth.views import auth_bp

app = Flask(__name__)

app.config.from_object(config.Config)

# registers app
db.init_app(app)
cors.init_app(app)
api.init_app(app)

# registers blueprint
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True, port=4444)
