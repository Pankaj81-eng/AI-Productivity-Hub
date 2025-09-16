import requests

response = requests.get("https://aiproductivityhub.openai.azure.com/", verify=False)
print(response.status_code)