import json
import boto3
import urllib.parse

sns = boto3.client('sns')

SNS_TOPIC_ARN = "SNS_ARN"

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    size = event['Records'][0]['s3']['object']['size']

    message = f"""
    📂 New File Uploaded!
    
    Bucket Name: {bucket}
    File Name: {key}
    File Size: {size} bytes
    """

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message,
        Subject="New File Uploaded to S3"
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Notification Sent!')
    }
