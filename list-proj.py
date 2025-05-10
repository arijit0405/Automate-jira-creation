# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://arijitchakraborty691.atlassian.net/rest/api/3/project"



API_Token= ""
auth = HTTPBasicAuth("arijitchakraborty691@gmail.com", API_Token )

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
projects = response.json()  

print("List of projects:")
for project in projects:
    print("- " + project["name"])
