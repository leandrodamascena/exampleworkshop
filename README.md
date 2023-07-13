# rafa-workshop

## Requirements

Python 3.10
SAM CLI
AWS CLI


## Building

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

1 - sam build
2 - sam local start-api

3 - mkdir -p /tmp/dynamodb
4 - cd /tmp/dynamodb
5 - docker run -d -v ${PWD}/docker:/home/dynamodblocal/data --name dynamodb-local -w /home/dynamodblocal -p 8000:8000 amazon/dynamodb-local:latest  -jar DynamoDBLocal.jar -sharedDb -dbPath ./data

## Running

1 - curl -H "Content-type: application/json" -X GET http://127.0.0.1:3000/bookings
2 - curl -H "Content-type: application/json" -X GET http://127.0.0.1:3000/flights
3 - curl -H "Content-type: application/json" -X GET http://127.0.0.1:3000/flights/{flight_id}
4 - curl -H "Content-type: application/json" -X PUT -d '{"x":"a"}' 'http://127.0.0.1:3000/bookings'
