import boto3

# Set the region 
region='us-west-2'

#set tag
environment_tag = 'DEV'

# creation EC2 client object
ec2_client = boto3.client('ec2', region_name=region)

# finds running instances that match environment_tag  
instances = ec2_client.describe_instances(Filters=[
    {'Name': 'tag:Environment', 'Values': [environment_tag]},
    {'Name': 'instance-state-name', 'Values': ['running']}
])

# list instances ids 
instance_ids = [instance['InstanceId'] for reservation in instances['Reservations'] for instance in reservation['Instances']]

# If there are running instances with the Environment: Dev tag, stop them
if len(instance_ids) > 0:
    ec2_client.stop_instances(InstanceIds=instance_ids)
    print(f'{len(instance_ids)} {environment_tag} instances stopped')
    for i in instance_ids:
        print(i)
else:
    print(f'no running {environment_tag} instances')