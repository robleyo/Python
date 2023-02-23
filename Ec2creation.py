import boto3
ec2_client=boto3.client("ec2")
ec2_client.create_instances(ImageId='ami-0f1a5f5ada0e7da53')
    InstanceType='t2.micro',
        MaxCount=1,
    MinCount=1,)|
    