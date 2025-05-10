import os
import json
import requests
from flask import Flask
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def createJira():
    url = "https://arijitchakraborty691.atlassian.net/rest/api/3/issue"

    JIRA_USER = os.getenv("JIRA_USER")
    API_Token = os.getenv("JIRA_API_TOKEN")
    auth = HTTPBasicAuth(JIRA_USER, API_Token)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "fields": {
            "project": {
                "key": "AR"
            },
            "summary": "First Jira Ticket Creation",
            "description": {
                "type": "doc",
                "version": 1,
                "content": [{
                    "type": "paragraph",
                    "content": [{
                        "type": "text",
                        "text": "My First Jira Ticket"
                    }]
                }]
            },
            "issuetype": {
                "id": "10011"
            }
        }
    })

    response = requests.post(
        url,
        headers=headers,
        data=payload,
        auth=auth
    )

    return json.dumps(response.json(), indent=4)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
