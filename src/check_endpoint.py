# filepath: c:\Users\PankajKumar\OneDrive - kyndryl\Documents\Automation and AI\AI-Productivity-Hub\src\check_endpoint.py
import requests
response = requests.get("https://api-nemo.openai.azure.com/")
print(response.status_code)