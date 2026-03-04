# 📂 Serverless File Upload Notification System

## 🚀 Project Overview

This project demonstrates a fully serverless, event-driven architecture built on AWS.

Whenever a file is uploaded to an Amazon S3 bucket, an AWS Lambda function is automatically triggered. The Lambda function extracts file metadata and sends a real-time email notification using Amazon SNS.

This project showcases core AWS serverless concepts including event triggers, IAM roles, and cloud monitoring.

---

## 🏗️ Architecture

### Flow

1. User uploads file to S3 bucket  
2. S3 triggers Lambda function  
3. Lambda processes file metadata  
4. Lambda publishes message to SNS  
5. SNS sends email notification  

Architecture:

S3 → Lambda → SNS → Email

---

## 🛠️ AWS Services Used

- Amazon S3 – Object storage
- AWS Lambda – Serverless compute
- Amazon SNS – Email notifications
- Amazon CloudWatch – Logs & monitoring
- AWS IAM – Role-based access control

---

## 📌 Features

- Fully serverless architecture
- Automatic scaling
- Real-time email alerts
- Event-driven processing
- IAM secure access
- CloudWatch logging enabled

---

## ⚙️ Lambda Function Code (Python)

```python
import json
import boto3
import urllib.parse
import os

sns = boto3.client('sns')

SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    size = event['Records'][0]['s3']['object']['size']

    message = f"""
    New File Uploaded!

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
```

---

## 🔐 IAM Permissions Required

### Lambda Execution Role

Attach:

- AWSLambdaBasicExecutionRole
- Custom policy with:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sns:Publish",
      "Resource": "YOUR_SNS_TOPIC_ARN"
    }
  ]
}
```

---

## 🚀 Setup Instructions

### Step 1: Create SNS Topic
- Create Standard topic
- Add Email subscription
- Confirm email subscription

### Step 2: Create Lambda Function
- Runtime: Python 3.x
- Add environment variable:
  - Key: SNS_TOPIC_ARN
  - Value: Your SNS Topic ARN
- Deploy function code

### Step 3: Create S3 Bucket
- Create unique bucket name
- Keep default settings

### Step 4: Add S3 Trigger
- Add S3 trigger to Lambda
- Select bucket
- Choose "All Object Create Events"

### Step 5: Test
- Upload a file to S3 bucket
- Check email for notification

---

## 🧠 Key Concepts Demonstrated

- Event-driven architecture
- Serverless computing
- IAM role configuration
- SNS topic publishing
- CloudWatch debugging
- Environment variable best practice

---


## 🔮 Future Enhancements

- Add DynamoDB for metadata storage
- Restrict file types (e.g., only PDF uploads)
- Integrate Slack webhook notifications
- Add SQS Dead Letter Queue
- Implement Infrastructure as Code (Terraform or CloudFormation)

