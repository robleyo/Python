import boto3
AWS_REGION = "us-west-2"
S3_BUCKET_NAME = "monbucket2231"
s3_resource = boto3.resource("s3", region_name=AWS_REGION)
s3_object = s3_resource.Object('monbucket2231', 'S3CreationDate.py')
    
s3_object.delete()
print('S3 object deleted')