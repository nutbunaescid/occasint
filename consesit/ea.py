import boto3
import json

def lambda_handler(event, context):
    bedrock = boto3.client('bedrock-runtime', region_name="us-east-1")
    
    # Construct the request body with the prompt
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": event["prompt"]  # Use the prompt from the event
                    }
                ]
            }
        ]
    })
    
    modelId = 'anthropic.claude-3-haiku-20240307-v1:0'  # Specify the Haiku model ID
    accept = 'application/json'
    contentType = 'application/json'
    
    # Invoke the model using the Bedrock API
    response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())
    answer = response_body["con"]  # Extract the generated response
    
    return {
        "statusCode": 200,
        "body": answer  # Return the generated response
    }
