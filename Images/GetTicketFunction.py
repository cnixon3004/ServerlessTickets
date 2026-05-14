import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    try:
        ticket_id = event.get('ticketId')

        response = table.get_item(
            Key={'ticketId': ticket_id}
        )

        item = response.get('Item')

        return {
            'statusCode': 200,
            'body': json.dumps(item)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }