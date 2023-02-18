import boto3
AWS_REGION = "us-west-2"
client = boto3.client("s3", region_name=AWS_REGION)
bucket_name = "yoroblebucket"
client.delete_bucket(Bucket=bucket_name)
print("Amazon S3 Bucket has been deleted")