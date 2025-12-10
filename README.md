# pytorch-scikit-learn-uv-docker-serverless-model-deployment-aws-lambda
Take Scikit-learn and Pytorch models and deploy it using docker on AWS lambda

I have used UV INIT locally to be able to use Python and Docker safely before deploying on AWS lambda


## Recommended workflow for ML model inference with Lambda

This is the cleanest setup if planning ML in Lambda:

-- Keep ML code + model in src/app/

-- Keep lambda handler minimal in src/lambda/

-- Develop/test locally using uv

-- Build a Docker container that wraps Lambda

-- Test container locally

-- Deploy container to AWS Lambda

-- Trigger via API Gateway

This gives us:

-- Full local reproducibility

-- No dependency hell

-- No AWS surprises

-- Easy commits to GitHub

## Docker

Build it:

docker build -t churn-prediction-lambda .

Run it:

docker run -it --rm -p 8080:8080  churn-prediction-lambda

Test it:

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

result = requests.post(url, json=customer).json()
print(result)
