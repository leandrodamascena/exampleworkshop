import json
import boto3

def lambda_handler(event, context):

    # EXAMPLE CONNECTION TO DDB LOCAL
    # For a Boto3 client.
    ddb = boto3.client('dynamodb', endpoint_url='http://YOURLOCALIP:8000')
    response = ddb.list_tables()
    print(response)


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello get flights",
            # "location": ip.text.replace("\n", "")
        }),
    }
