import boto3
s3_resource=boto3.client
s3_resource=boto3.client("s3")
s3_resource.list_buckets()["Buckets"][0]["Name"]
'monbucket2231'
creation_date=s3_resource.list_buckets()["Buckets"][0]["CreationDate"]
creationdate.strftime("%d%m%y%H:%M:%s")
'260720_11:03:1595757811'
for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])