import json

def show(event, context):
    response = {
        "statusCode": 200,
        "body": json.dumps('Hello Python')
    }

    return response

def create(event, context):
    response = {
        "statusCode": 200,
        "body": json.dumps('Hello Python')
    }

    return response