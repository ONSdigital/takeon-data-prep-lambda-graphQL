import os
import boto3
from botocore.exceptions import ClientError


def send_to_wrangler_queue(config_data):
    print(f'Validation config data placed on wrangler queue')
    return send_to_queue(os.getenv("OUTPUT_QUEUE_URL"), config_data)


def send_to_error_queue(error_message):
    print(f'Placing error details on error queue')
    return send_to_queue(os.getenv("ERROR_QUEUE_URL"), error_message)


def send_to_queue(queue, message):
    sqs_client = boto3.client('sqs')
    try:
        msg = sqs_client.send_message(QueueUrl=queue, MessageBody=message)
    except ClientError as e:
        print(f'Error sending message to queue {e}')
        return None
    return msg
