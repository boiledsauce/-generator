# cover-letter-generation-service

## Introduction

This is a service that will take a string of the job description of your likings, along with your uploaded cover letters that you place in the folder cover_letters as .txt files.

It will then generate with the help of GPT-4-Turbo a brand-new cover-letter in respect to:

- Your CV
- Your writing style in the cover letters you have already written
- The job's description

## Prerequisites

The prerequisites for setting up the cover letter generation service are as follows:

- Kubernetes running of any kind. I use Kubernetes In Docker (KIND).
- A Kubernetes cluster up and running
- Docker
- An OpenAI API-Key

Make sure you have these prerequisites installed before proceeding with the setup.

## Setup

To set up the cover letter generation service, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/wille/projects/cover-letter-generation-service.git
   ```

2. Navigate to the project directory:
   create a `secret.yaml` inside of `k8s/` with your openAI API key

   ```
   apiVersion: v1
   kind: Secret
   metadata:
   name: openai-api-secret
   type: Opaque
   stringData:
   api-key: `<YOUR_API_KEY_HERE>
   ```

3. Create a folder called `cover_letters` in the main directory.
   Paste all your written cover_letters that you have written so far that you deem good enough

4. `kubectl config use-context my-cluster-name`

5. Run the k8s setup

`./deploy.sh`

6. Set up the ports for external access:

`kubectl <pod_name> port-forward 8000:8000`

7.  Access the endpoint:
    `POST http://127.0.0.1:8000/generate`

Body should contain a json object of:

```
- cv: A large string of your content of your CV
- job_description: A large string of the job's descriptio
```

`Response: 200 OK - A generated Cover letter as a string`
