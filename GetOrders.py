import json
import boto3
from decimal import Decimal

# Pastikan region benar
dynamodb = boto3.resource('dynamodb', region_name="us-east-1")  
table = dynamodb.Table("Orders")  # Ganti dengan nama tabel DynamoDB kamu

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)  # Convert Decimal ke float
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    try:
        response = table.scan()  # Scan semua data dari tabel
        orders = response.get("Items", [])  # Ambil data (kalau kosong tetap [])

        return {
            'statusCode': 200,
            'headers': {
                "Content-Type": "application/json"
            },
            'body': json.dumps(orders, cls=DecimalEncoder)  # Convert data ke JSON
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }