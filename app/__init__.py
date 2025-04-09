from flask import Flask
from flask_cors import CORS
from .routes import task_routes
from flasgger import Swagger

import os

def create_app():
    app = Flask(__name__)

    origins = os.getenv("FRONTEND_ORIGINS", "http://localhost:5174").split(",")

    CORS(app, origins=origins, supports_credentials=True, allow_headers=[
        "Content-Type", 
        "Authorization", 
        "X-Amz-Date",
        "X-Api-Key",
        "X-Amz-Security-Token"
    ], methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH", "HEAD"])

    Swagger(app)
    app.register_blueprint(task_routes)
    return app