import os
import requests

def trigger_jenkins_job(job_name):
    JENKINS_URL = os.getenv("JENKINS_URL")
    JENKINS_USER = os.getenv("JENKINS_USER")
    JENKINS_TOKEN = os.getenv("JENKINS_TOKEN")
    ENV_NAME = os.getenv("ENV_NAME")
    RELEASE_TAG = os.getenv("RELEASE_TAG")

    url = f"{JENKINS_URL}/job/{job_name}/build"
    auth = (JENKINS_USER, JENKINS_TOKEN)
    data = {
        "parameter": [
            {"name": "ENV_NAME", "value": ENV_NAME},
            {"name": "RELEASE_TAG", "value": RELEASE_TAG}
        ]
    }

    response = requests.post(url, auth=auth, json=data)
    print(f"Triggered Jenkins job: {job_name}, Status Code: {response.status_code}")

if __name__ == "__main__":
    trigger_jenkins_job("IACX-AEM")
    trigger_jenkins_job("IACX-ADAPTOR")
    trigger_jenkins_job("IACX-REVERSE-PROXY")
