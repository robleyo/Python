import boto3

AWS_REGION = "us-west-2"
resource = boto3.resource("s3", region_name=AWS_REGION)
bucket_name = "monbucket2231"
location = {'LocationConstraint': AWS_REGION}
bucket = resource.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration=location)
print("S3 bucket created")

