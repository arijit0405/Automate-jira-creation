
# GitHub to Jira Ticket Automation - Project Summary

## Objective:
Automatically create a Jira ticket whenever a comment is added to a GitHub issue using webhooks and a Flask app hosted on AWS EC2.

---

## Step-by-Step Overview

### 1. Created a Python Flask App
- Built a Flask API endpoint `/createJira` that listens for POST requests.
- Used the `requests` library to call Jira's REST API.
- Hardcoded the Jira API token and email (later this will be moved to a .env file for security).

### 2. Tested the Flask App Locally on EC2
- Ensured Python 3 was installed.
- Ran the script using `python3 github-jira-ticket.py` with Flask listening on `0.0.0.0:5000` to expose to public IP.

### 3. Created an EC2 Instance (AWS)
- Launched a t2.micro EC2 instance on AWS.
- Deployed the Flask app on this instance.
- Made sure Flask server was running using the public DNS and port 5000.

### 4. Configured Security Group
- Opened **port 5000** to allow external access via HTTP.
- Added inbound rule in EC2 security group: TCP | 5000 | 0.0.0.0/0.

### 5. Created GitHub Webhook
- Added webhook to GitHub repo with the payload URL pointing to the EC2 instance: 
  `http://<EC2-PUBLIC-DNS>:5000/createJira`
- Set event trigger to `issue_comment`.

### 6. Faced and Resolved Issues
- Encountered `IndentationError`: fixed incorrect indentation in Python script.
- Faced connection issues: fixed by verifying Flask was running and EC2 port was open.

### 7. Verified Integration
- Sent test comment on GitHub issue.
- Verified Jira ticket was automatically created from GitHub event.

---


---

Author: arijit0405
Project: Automate-jira-creation
