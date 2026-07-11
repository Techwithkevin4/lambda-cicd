import json

def lambda_handler(event, context):
    return{
        'statusCode' : 200,
        'body': json.dump('Hello from our CICD github actions workflow vscode')
    }