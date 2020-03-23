import boto3
import os
client = boto3.client('ssm')
def lambda_handler(event, context):
	response = client.get_parameter(Name='UserName')
	result = response['Name']['Value']
s3 = boto3.client('s3')
bucket_name = os.environ['user-value'] # Supplied by Function service-discovery wire

def handler(message, context):
	response = s3.put_object(
	Bucket=bucket_name,
	Key='SSM-parameters',
	Body=result,
	ACL='public-read'
	)
	return response
