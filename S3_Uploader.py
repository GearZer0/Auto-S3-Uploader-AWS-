import os
import boto3

client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)

for file in os.listdir():
        upload_file_bucket = 'Tool'
        upload_file_key = 'python/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)
