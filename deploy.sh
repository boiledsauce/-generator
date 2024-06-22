# #!/bin/bash

# Build the Docker image
docker build -t cover-letter-generator-image:latest .

# Load the Docker image into kind
kind load docker-image cover-letter-generator-image:latest --name kind-cluster

# Restart the deployment
kubectl rollout restart deployment cover-letter-generator-deployment

POD_NAME=$(kubectl get pods --namespace default -l "app=cover-letter-generator" -o jsonpath="{.items[0].metadata.name}")
kubectl port-forward $POD_NAME 8000:8000

# Apply the Kubernetes configuration
kubectl apply -f k8s/
