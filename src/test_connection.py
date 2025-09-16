import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

try:
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    )
    deployment_id = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
    response = client.chat.completions.create(
        model=deployment_id,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say hello!"}
        ],
        max_completion_tokens=100
    )
    print("Connection successful!")
    print("Response:", response.choices[0].message.content)
except Exception as e:
    print("Connection failed!")
    print(e)