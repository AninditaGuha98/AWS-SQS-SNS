import boto3

sqs=boto3.client('sqs')

# print(response)

response = sqs.send_message(
    QueueUrl="https://sqs.us-east-1.amazonaws.com/886627555245/test",
    MessageBody="serverless"
)

print(response)


