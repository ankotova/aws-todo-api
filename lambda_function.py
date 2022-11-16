""" CRUD ToDo API"""
import json
import logging
import uuid
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')
table = dynamodb.Table('TODO')


def lambda_handler(event, context):
    logger.info(event)
    http_method = event['httpMethod']
    path = event['path']
    try:
        if http_method == 'POST':
            try:
                response = save_todo(json.loads(event['body']))
            except KeyError:
                return build_response(400, {'Error': 'There was an error when creating the ToDo object.'})
        elif http_method == 'GET':
            if path == '/todo':
                response = get_todos()
            else:
                response = get_todo(event['pathParameters']['todo_id'])
        elif http_method == 'PUT':
            request_body = json.loads(event['body'])
            try:
                response = modify_todo(event['pathParameters']['todo_id'], request_body['title'], request_body['description'])
            except KeyError:
                return build_response(400, {'Error': 'There was an error while updating a ToDo object.'})
        elif http_method == 'DELETE':
            response = delete_todo(event['pathParameters']['todo_id'])
        else:
            response = build_response(404, 'Not found')
    except ClientError as e:
        if e.response['Error']['HTTPStatusCode'] == 400:
            return build_response(400, {'Error': 'There was an error while interacting with ToDo API.'})
        else:
            return build_response(e.response['Error']['HTTPStatusCode'], {"Unexpected error: %s" % e})
    return response


def save_todo(request_body):
    """ Save new ToDo to DynamoDb """
    saved_todo = {
        'id': str(uuid.uuid4()),
        'title': request_body['title'],
        'description': request_body['description']
    }
    table.put_item(Item=saved_todo)
    body = {
        'Message': 'ToDo object created successfully.',
        'Item': saved_todo
    }
    return build_response(200, body)


def get_todos():
    """ Get list of all the ToDos from DynamoDB table"""
    response = table.scan()
    result = response['Items']
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        result.extend(response['Items'])
    body = {
        'todo': result
        }
    return build_response(200, body)


def get_todo(todo_id):
    """ Get ToDo from DynamoDB table by its ID"""
    response = table.get_item(
        Key={
            'id': todo_id
        }
    )
    if 'Item' in response:
        return build_response(200, response['Item'])
    else:
        return build_response(404, {'Error': 'The object with the provided ID could not be found.'})


def modify_todo(todo_id, update_title, update_description):
    """ Modify ToDo in DynamoDB table by its ID"""
    response = table.get_item(
        Key={
            'id': todo_id
        })
    if 'Item' in response:
        response = table.update_item(
            Key={
                'id': todo_id
            },
            UpdateExpression='set title = :t, description = :d',
            ExpressionAttributeValues={
                ':t': update_title,
                ':d': update_description
            },
            ReturnValues='UPDATED_NEW'
        )
        body = {
            'Message': 'ToDo object updated successfully.'
        }
        return build_response(200, body)
    else:
        return build_response(404, {'Error': 'The object with the provided ID could not be found.'})


def delete_todo(todo_id):
    """ Delete ToDo from DynamoDB table by its ID"""
    response = table.get_item(
        Key={
            'id': todo_id
        })
    if 'Item' in response:
        response = table.delete_item(
            Key={
                'id': todo_id
                },
            ReturnValues='ALL_OLD'
        )
        body = {
            'Message': 'ToDo object deleted successfully.',
        }
        return build_response(200, body)
    else:
        return build_response(404, {'Error': 'The object with the provided ID could not be found.'})


def build_response(status_code, body=None):
    """ Handle final response """
    response = {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    if body is not None:
        response['body'] = json.dumps(body)
    return response
