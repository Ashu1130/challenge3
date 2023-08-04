import boto3
import json

def get_instance_metadata():
    # Create a Boto3 EC2 client
    ec2_client = boto3.client('ec2')

    # Get the instance ID of the current EC2 instance (this code must be running on an EC2 instance)
    response = ec2_client.describe_instances(InstanceIds=['self'])
    instance_id = response['Reservations'][0]['Instances'][0]['InstanceId']

    # Get the instance metadata
    response = ec2_client.describe_instances(InstanceIds=[instance_id])

    # Extract relevant information from the response
    instance_metadata = {
        'InstanceId': response['Reservations'][0]['Instances'][0]['InstanceId'],
        'InstanceType': response['Reservations'][0]['Instances'][0]['InstanceType'],
        'PrivateIpAddress': response['Reservations'][0]['Instances'][0]['PrivateIpAddress'],
        # Add more metadata fields as needed
    }

    # Convert the metadata to JSON format
    json_output = json.dumps(instance_metadata, indent=4)
    return json_output
