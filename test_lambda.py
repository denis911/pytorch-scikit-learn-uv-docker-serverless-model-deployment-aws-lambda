import boto3
import json
from botocore.config import Config

session = boto3.Session(profile_name="lambda-dev")

lambda_client = session.client(
    "lambda",
    region_name="eu-central-1",
)

def invoke_lambda(a, b):
    payload = {
        "a": a,
        "b": b
    }

    response = lambda_client.invoke(
        FunctionName="add_number_denis911",
        InvocationType="RequestResponse",
        Payload=json.dumps(payload)
    )

    result = json.loads(response["Payload"].read())
    return result

if __name__ == "__main__":
    out = invoke_lambda(10, 20)
    print(out)
