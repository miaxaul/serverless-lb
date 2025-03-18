import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    
    order_id = str(uuid.uuid4())
    order_item = {
        'order_id': order_id,
        'name': body['name'],
        'food': body['food'],
        'quantity': body['quantity']
    }
    
    table.put_item(Item=order_item)
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Order placed!', 'order_id': order_id})
    }