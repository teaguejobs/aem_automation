import os
import boto3

ssm = boto3.client('ssm', region_name='us-east-1')

PARAMETERS = {
    "publishaem": {
        "/SG/PPXX/AEMPUBLISH/ADMIN_PASSWORD": "securePassword123",
        "/SG/PPXX/AEMPUBLISH/SSLKEYSTOREPASSWORD": "keystorePass123"
    },
    "aem-adaptor": {
        "/SG/PPXX/ADAPTOR/KEYSTOREPASSWORD": "keyPass123",
        "/SG/PPXX/ADAPTOR/SSLKEYSTOREPASSWORD": "sslKeyPass123",
        "/SG/PPXX/ADAPTOR/SPM_PASSWORD": "spmPass123",
        "/SG/PPXX/ADAPTOR/SPM_USERNAME": "spmUser",
        "/SG/PPE/ADAPTOR/DB_PASSWORD": "dbPass123",
        "/SG/PPE/ADAPTOR/SMS_TEMPLATEID": "sms123",
        "/SG/PPE/ADAPTOR/EMAIL_TEMPLATEID": "email123",
        "/SG/PPE/ADAPTOR/NOTIFY_APIKEY": "notifyApiKey123"
    }
}

def create_params():
    for group, params in PARAMETERS.items():
        for name, value in params.items():
            ssm.put_parameter(
                Name=name,
                Value=value,
                Type="SecureString",
                Overwrite=True
            )
            print(f"Parameter created: {name}")

if __name__ == "__main__":
    create_params()
