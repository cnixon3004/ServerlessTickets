import json
import boto3
import uuid
from datetime import datetime
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        issue = body.get('issue', 'No issue provided')

        ticket_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()

        item = {
            'ticketId': ticket_id,
            'issue': issue,
            'status': 'OPEN',
            'createdAt': timestamp
        }

        table.put_item(Item=item)

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Ticket created',
                'ticketId': ticket_id
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
