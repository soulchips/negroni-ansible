import boto3
t = boto3.resource('s3')
for b in t.buckets.all():
    print(b.name)