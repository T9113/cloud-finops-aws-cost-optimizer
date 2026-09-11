import boto3

ec2 = boto3.client('ec2')
eips = ec2.describe_addresses()

print('--- Unattached (Costly) Elastic IPs ---')
for ip in eips['Addresses']:
    if 'InstanceId' not in ip:
        print(f"Unattached IP: {ip['PublicIp']}, AllocationId: {ip.get('AllocationId')}")
