# === PowerShell-friendly version of deploy.sh script (deploy.ps1) ===

# ==========================
# Deploy script for Windows PowerShell
# Builds Docker image, pushes to ECR, updates Lambda
# ==========================

# --- Config ---
$IMAGE_NAME = "churn-prediction-lambda"
$AWS_REGION = "eu-central-1"

# Get AWS account ID
$AWS_ACCOUNT_ID = (aws sts get-caller-identity | jq -r ".Account")

# Get latest commit SHA and current datetime
$COMMIT_SHA = (git rev-parse --short HEAD)
$DATETIME = Get-Date -Format "yyyyMMdd-HHmmss"
$IMAGE_TAG = "$COMMIT_SHA-$DATETIME"

$ECR_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
$IMAGE_URI = "${ECR_URI}/${IMAGE_NAME}:${IMAGE_TAG}"

# --- Optional: create ECR repo (run only once) ---
# aws ecr create-repository --repository-name $IMAGE_NAME --region $AWS_REGION

# --- Docker login to ECR ---
aws ecr get-login-password --region $AWS_REGION |
docker login --username AWS --password-stdin "$ECR_URI"

# --- Build Docker image ---
docker build -t "${IMAGE_NAME}:${IMAGE_TAG}" .

# --- Tag image for ECR ---
docker tag "${IMAGE_NAME}:${IMAGE_TAG}" "${IMAGE_URI}"

# --- Push image to ECR ---
docker push "${IMAGE_URI}"

# --- Update Lambda function ---
aws lambda update-function-code `
  --function-name churn-prediction `
  --image-uri "${IMAGE_URI}" `
  --region $AWS_REGION

Write-Host "Deployment completed: $IMAGE_URI"


