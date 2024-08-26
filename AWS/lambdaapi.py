import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    httpmethod = event['httpMethod']
    client = boto3.client('iot-data', region_name='ap-south-1')
    print(httpmethod)
    if httpmethod=="POST":
        body="i am in post method"
        json_data = json.loads(event['body'])
        res = client.publish(
            topic='$aws/things/rushilThing/shadow/update/delta',
            qos=1,
            payload=json.dumps(json_data)
        )

        
        
    else:
        body="i am not in post method"
    return {
        'statusCode': 200,
        'body': json.dumps(json_data)
    }
