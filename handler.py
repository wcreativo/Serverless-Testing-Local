import json
import logging

try:
    import unzip_requirements
except ImportError:
    pass

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodbTableName = "usersTable"
dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:8000")
table = dynamodb.Table(dynamodbTableName)


def get_users(event, context):
    try:
        response = table.scan()
        if "Items" in response:
            return {"status_code": 200, "body": json.dumps(response["Items"])}
        return {}
    except:
        logger.exception("Log it here for now")
