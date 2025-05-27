# Automated AEM Build Process

Introduced to reduce manual intervention during AEM environment setup.

## Steps

1. **Branch Creation & MR**
   - Script auto-creates feature branch from `master`
   - Updates YAML files with correct release tag
   - Opens MR in GitLab with standardized title

2. **AWS Parameter Store Setup**
   - Checks and creates secure parameters in AWS SSM
   - Ensures all required keys are present

3. **IaC Pipeline Trigger**
   - Triggers Jenkins jobs for:
     - AEM Publish
     - AEM Adaptor
     - Reverse Proxy

4. **Promotion to Staging Environments**
   - Manual approval gates for TST and PPE
   - Version tags auto-increment per stage

## Prerequisites

| System | Required |
|--------|----------|
| GitLab API Token | ✅ |
| Jenkins User + Token | ✅ |
| AWS IAM Access Key | ✅ |
| Python 3.11+ | ✅ |
