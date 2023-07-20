import os
import requests
import json

api_key = os.getenv("APOLLO_IO_API_KEY")

if not api_key:
    print("Please set the APOLLO_IO_API_KEY environment variable.")
    exit(1)

url = "https://api.apollo.io/v1/mixed_people/search"
headers = {
    "Content-Type": "application/json",
    "Cache-Control": "no-cache",
}
data = {
    "api_key": api_key,
    "q_organization_domains": "apollo.io\ngoogle.com",
    "page" : 1,
    "person_titles" : ["sales manager", "engineer manager"]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

# Handle the response
if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed with status {response.status_code}")
