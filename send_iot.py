import greengrasssdk
import json
import time
from datetime import datetime
from datetime import timedelta
#import boto3
client = greengrasssdk.client('iot-data')

temperature_count = 0
temperature_sum = 0
pressure_sum = 0
five_min = datetime.now() + timedelta(seconds=30)

def function_handler(event, context):
        global temperature_sum, temperature_count, pressure_sum, five_min
        temperature_sum += event["temperature"] 
        pressure_sum += event["pressure"]
        temperature_count += 1
        
        if datetime.now() > five_min:
            temperature_average = temperature_sum/temperature_count
            pressure_average = pressure_sum/temperature_count
            temperature_count = 0
            temperature_sum = 0
            pressure_sum = 0
            timestamp = str(datetime.utcnow())
            message={}
            message['temperature'] = temperature_average
            message['pressure'] = pressure_average
            message['time'] = timestamp
            message['id'] = event["id"]
            message['lambda'] = event["id"]
            response=client.publish(
                topic='hello/world/pubsub2',
                qos=0,
                payload=json.dumps(message)
            )
            five_min = datetime.now() + timedelta(seconds=300)
        
