# cover-letter-generation-service

## Setup

To set up the cover letter generation service, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/wille/projects/cover-letter-generation-service.git
   ```

2. Navigate to the project directory:
   create a secret.yaml inside of k8s/ with your openAI api key
   apiVersion: v1
   kind: Secret
   metadata:
   name: openai-api-secret
   type: Opaque
   stringData:
   api-key: <YOUR_API_KEY_HERE>

3. Create a folder called cover_letters in the main directory
   Paste all your written cover_letters that you have written so far that you deem good enough

4. Run the k8s setup

```
./deploy.sh
```

5.

Set up the ports for external access:
`
kubectl <pod_name> port-forward 8000:8000

```

Access the endpoint:
POST http://127.0.0.1:8000/generate

Body should contain a json object of:
```

- cv: A large string of your content of your CV
- job_description: A large string of the job's descriptio

```
Response: 200 OK - A generated Cover letter as a string
```
