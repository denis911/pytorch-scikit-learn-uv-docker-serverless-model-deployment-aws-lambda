import boto3
import json

# Create a Lambda client using your AWS profile + region
lambda_client = boto3.client(
    "lambda",
    region_name="eu-central-1",   # Frankfurt
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
