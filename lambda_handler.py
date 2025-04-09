from app import create_app
from aws_lambda_wsgi import response

flask_app = create_app()

def lambda_handler(event, context):
    return response(flask_app, event, context)