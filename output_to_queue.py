# Function to send data to queue
import boto3

def output_to_queue(output):
    queue_url = os.getenv("OUTPUT_QUEUE_URL")
    sqs = boto3.client("sqs")
    sqs.send_message(QueueUrl=queue_url, MessageBody=json.dumps(output))
