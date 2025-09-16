import os
import ssl
import urllib3
from dotenv import load_dotenv

# Disable SSL warnings and verification
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

load_dotenv()

from openai import AzureOpenAI
import httpx

def summarize_text(text):
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        http_client=httpx.Client(verify=False)
    )

    deployment_id = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
    prompt = f"Summarize the following text:\n{text}"

    response = client.chat.completions.create(
        model=deployment_id,
        messages=[
            {"role": "system", "content": "Please provide a concise summary of the following text:"},
            {"role": "user", "content": prompt}
        ],
        max_completion_tokens=300
    )
    #    print("Full response:", response)  # <-- Add this line here
    summary = response.choices[0].message.content
    return summary