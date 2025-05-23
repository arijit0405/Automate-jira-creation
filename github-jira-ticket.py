import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def createJira():
    url = "https://arijitchakraborty691.atlassian.net/rest/api/3/issue"

    # Your Jira API token and email (you can later move to .env)
    API_Token = ""
    JIRA_Email = "arijitchakraborty691@gmail.com"

    auth = HTTPBasicAuth(JIRA_Email, API_Token)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "fields": {
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": "My First Jira Ticket",
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    }
                ],
                "type": "doc",
                "version": 1
            },
            "issuetype": {
                "id": "10011"
            },
            "project": {
                "key": "AR"
            },
            "summary": "First Jira Ticket Creation"
        }
    })

    response = requests.post(
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(response.json(), indent=4)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
