from app import create_app
from aws_lambda_wsgi import response

flask_app = create_app()

def lambda_handler(event, context):
    
    event['headers'] = event.get('headers') or {}
    event['headers'].setdefault('Content-Type', 'application/json')
    
    if 'queryStringParameters' not in event:
        event['queryStringParameters'] = None

    if 'requestContext' not in event:
        event['requestContext'] = {"protocol": "HTTP/1.1"}
        
    if 'Host' not in event['headers']:
        event['headers']['Host'] = "localhost"

    event['headers']['X-Forwarded-Proto'] = 'https'
    
    return response(
        flask_app, 
        event, 
        context
    )