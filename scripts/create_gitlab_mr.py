import os
import requests
from git import Repo

GITLAB_TOKEN = os.getenv("GITLAB_API_TOKEN")
PROJECT_ID = os.getenv("GITLAB_PROJECT_ID")
BASE_URL = f"https://gitlab.ce.com.sss.int/api/v4/projects/ {PROJECT_ID}"

def create_branch(branch_name):
    url = f"{BASE_URL}/repository/branches?branch={branch_name}&ref=master"
    headers = {"PRIVATE-TOKEN": GITLAB_TOKEN}
    response = requests.post(url, headers=headers)
    return response.json()

def create_merge_request(title, source_branch):
    url = f"{BASE_URL}/merge_requests"
    headers = {"PRIVATE-TOKEN": GITLAB_TOKEN}
    data = {
        "source_branch": source_branch,
        "target_branch": "master",
        "title": title
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()

if __name__ == "__main__":
    TICKET_NUMBER = os.getenv("TICKET_NUMBER")
    ENV_NAME = os.getenv("ENV_NAME")
    BRANCH_NAME = f"feature/{TICKET_NUMBER}"
    MR_TITLE = f"Feat: {TICKET_NUMBER} | {ENV_NAME}"

    create_branch(BRANCH_NAME)
    mr_response = create_merge_request(MR_TITLE, BRANCH_NAME)
    print("Merge Request Created:", mr_response.get("web_url"))
