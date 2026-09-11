import boto3

ec2 = boto3.client('ec2')
volumes = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])

print('--- Unattached (Idle) EBS Volumes ---')
for v in volumes['Volumes']:
    print(f"Volume ID: {v['VolumeId']}, Size: {v['Size']} GB, Type: {v['VolumeType']}")
