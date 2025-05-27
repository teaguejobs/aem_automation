# AEM Environment Automation Tool

Automates the deployment of AEM environments by reducing manual steps.

## Features

- Auto-create Git branches and Merge Requests in GitLab
- Auto-generate AWS SSM Parameters
- Trigger Jenkins IaC pipelines for AEM Publish, Adaptor, and Reverse Proxy
- Dev-first workflow with promotion to TST and PPE

## Prerequisites

- Python 3.11
- GitLab API Token
- Jenkins API Access
- AWS Credentials (for SSM access)

## Usage

1. Copy `.env.example` to `.env` and fill in values.
2. Run locally or via Docker:

```bash
docker run --env-file .env aem-env-builder
# aem_automation
