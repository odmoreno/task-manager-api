from flask import Flask
from flask_cors import CORS
from .routes import task_routes
from flasgger import Swagger

import os

def create_app():
    app = Flask(__name__)

    CORS(app, resources={r"/*": {
        "origins": os.getenv("FRONTEND_ORIGINS", "*").split(","),
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }})
    
    Swagger(app)
    app.register_blueprint(task_routes)
    return app
