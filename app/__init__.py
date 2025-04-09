from flask import Flask
from .routes import task_routes
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    Swagger(app)
    app.register_blueprint(task_routes)
    return app