from app import create_app
from aws_lambda_wsgi import response

flask_app = create_app()

def lambda_handler(event, context):
    if 'queryStringParameters' not in event:
        event['queryStringParameters'] = None

    if 'requestContext' not in event:
        event['requestContext'] = {"protocol": "HTTP/1.1"}

    if 'headers' not in event:
        event['headers'] = {}
    if 'Host' not in event['headers']:
        event['headers']['Host'] = "localhost"

    
    return response(
        flask_app, 
        event, 
        context,
        environ_builder_kwargs={"wsgi.url_scheme": "https"}
    )