import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb', region_name='us-west-2')
    client = boto3.client('iot-data')
    dynamodb.put_item(
        TableName='ArturotestTemp2',
         Item={
          'Id':{"S":str(event['id'])},
          'Timestamp':{"S":str(event['time'])},
          'Pressure':{"S":str(event['pressure'])},
          'Temperature':{"S":str(event['temperature'])},
         }
     )  
    response=client.publish(topic='arturo/republish2', qos=0, payload=json.dumps({"uploaded":"dynamoDB"}))
    return {
        'statusCode': 200,
        'body': event["temperature"]
    }
