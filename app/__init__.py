from flask import Flask
from flask_cors import CORS
from .routes import task_routes
from flasgger import Swagger

import os

def create_app():
    app = Flask(__name__)

    #origins_raw = os.getenv("FRONTEND_ORIGINS")
    #origins = origins_raw.split(",") if origins_raw else ["*"]

    CORS(app, resources={r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
    }})
    
    Swagger(app)
    app.register_blueprint(task_routes)
    return app
