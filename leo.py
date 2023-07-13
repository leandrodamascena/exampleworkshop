import boto3

## For a Boto3 client ('client' is for low-level access to Dynamo service API)
ddb1 = boto3.client('dynamodb', endpoint_url='http://localhost:8000', region_name='us-east-1')
response = ddb1.list_tables()
print(response)
