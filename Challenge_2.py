#Pythonv script to query AWS instance metadata and format the output as JSON.
#AWS provides a special URL for instance metadata that you can access from within an EC2 instance. Here's a Python script to achieve this:

import requests
import json

def get_instance_metadata():
    # Define the AWS instance metadata URL
    metadata_url = "http://169.254.169.254/latest/meta-data/"

    # List of metadata fields you want to retrieve
    metadata_fields = [
        "instance-id",
        "instance-type",
        "ami-id",
        "local-ipv4",
        "public-ipv4",
        "availability-zone",
        "region",
    ]

    metadata = {}

    try:
        for field in metadata_fields:
            url = metadata_url + field
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                metadata[field] = response.text
            else:
                metadata[field] = "N/A"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching metadata: {e}")
        return None

    return metadata

if __name__ == "__main__":
    instance_metadata = get_instance_metadata()
    if instance_metadata:
        # Convert the metadata to JSON format
        json_output = json.dumps(instance_metadata, indent=4)
        print(json_output)
