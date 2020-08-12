import json
from user_numpy import UserNumpy

def lambda_handler(event, context):
    un = UserNumpy()

    un_str = [str(n) for n in un.array()]
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": ','.join(un_str)
        }),
    }