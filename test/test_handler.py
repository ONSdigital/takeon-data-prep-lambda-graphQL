from handler import extract_json_from_eventbody
import pytest


aws_event = {'Records': [
        {
            'messageId': 'id',
            'receiptHandle': 'handle',
            'body': '{"reference":"77700000001","period":"201803","survey":"066","bpmId":"12345"}',
            'attributes':
                {
                    'ApproximateReceiveCount': '1',
                    'AWSTraceHeader': 'Root=id',
                    'SentTimestamp': '1579694628993',
                    'SenderId': 'SenderID',
                    'ApproximateFirstReceiveTimestamp': '1579694628997'
                },
            'messageAttributes': {},
            'md5OfBody': 'md50hash',
            'eventSource': 'aws:sqs',
            'eventSourceARN': 'sourceARN',
            'awsRegion': 'eu-west-2'
        }]
    }


def test_extract_json_from_eventbody_givenvaliddata_givesexpectedoutput():
    expected_output = {"reference": "77700000001", "period": "201803", "survey": "066", "bpmId": "12345"}
    assert extract_json_from_eventbody(aws_event) == expected_output
