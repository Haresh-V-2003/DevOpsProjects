import requests
import json
from requests.auth import HTTPBasicAuth

# Replace these with your actual details
organization = 'your_organization'  # Azure DevOps organization
project = 'your_project'            # Azure DevOps project name
pipeline_id = 'your_pipeline_id'    # Pipeline ID or name
pat = 'your_personal_access_token'  # Personal Access Token (PAT)

# URL for triggering the pipeline
url = f'https://dev.azure.com/{organization}/{project}/_apis/pipelines/{pipeline_id}/runs?api-version=7.1-preview.1'

# Define your runtime variables (key-value pairs)
runtime_variables = {
    "organization": "your_organization_name",  # Replace with the actual organization value
    "access_level": "your_access_level",      # Replace with the actual access level
    "group_name": "your_group_name",          # Replace with the actual group name
    "project_name": "your_project_name"       # Replace with the actual project name
}

# Prepare the payload with runtime variables
payload = {
    "variables": runtime_variables
}

# Make the POST request to trigger the pipeline
response = requests.post(
    url,
    headers={'Content-Type': 'application/json'},
    auth=HTTPBasicAuth('', pat),  # Authentication with PAT
    data=json.dumps(payload)      # Send the payload as JSON
)

# Check the response status
if response.status_code == 200:
    print(f"Pipeline triggered successfully! Run details: {response.json()}")
else:
    print(f"Failed to trigger pipeline. Status code: {response.status_code}, Response: {response.text}")
