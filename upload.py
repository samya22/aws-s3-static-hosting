import boto3

s3 = boto3.client('s3')

bucket_name = 'my-static-website-bucket'

file_name = 'index.html'

s3.upload_file(file_name, bucket_name, file_name)

print("Website uploaded successfully to S3 bucket")