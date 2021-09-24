import json
import boto3
from botocore.vendored import requests
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
s3 = boto3.resource('s3')
bucket = 'your bucket name'
filename = ' your file name'

def lambda_handler(event, context):
''' KnowBe4 - Demonstrates a simple HTTP request from Lambda '''
    headers={"Authorization": "ACCOUNT TOKEN"}
    response = requests.get('https://eu.api.knowbe4.com/v1/users',headers=headers)
    users = json.loads(response.text) 
    logger.debug('users are  = {}'.format(type(users)))

    put_object_on_s3(bucket, filename, users)

    return True

def put_object_on_s3(bucket, filename,json_data ):

    try:
        s3object = s3.Object(bucket, filename, json_data)
        s3object.put(Body=(bytes(json.dumps(json_data).encode('UTF-8'))))
        logger('put_object_on_s3', 'Users successfully created  ', severity='INFO')
    except:
        logger('put_object_on_s3', 'Unable to create the users.',severity='ERROR')
