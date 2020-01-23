import os
import boto3
from botocore.exceptions import ClientError


def send_to_wrangler_queue(config_data):
    return send_to_queue(QueueUrl=os.getenv("OUTPUT_QUEUE_URL"), MessageBody=config_data)


def send_to_error_queue(error_message):
    return send_to_queue(QueueUrl=os.getenv("ERROR_QUEUE_URL"), MessageBody=error_message)


def send_to_queue(queue, message):
    sqs_client = boto3.client('sqs')
    try:
        msg = sqs_client.send_message(QueueUrl=queue, MessageBody=message)
    except ClientError as e:
        f'Error sending message to queue {e}'
        return None
    return msg
