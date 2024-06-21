# #!/bin/bash

# Build the Docker image
docker build -t cover-letter-generator-image:latest .

# Load the Docker image into kind
kind load docker-image cover-letter-generator-image:latest --name kind-cluster

# Apply the Kubernetes configuration
kubectl apply -f k8s/