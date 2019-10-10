from parse_validation_data import parse_validation_data
import json
import boto3
import os
import requests

# Set up clients
sqs = boto3.client('sqs')

business_layer_endpoint = 'http://acd672ad1dba911e9b80c06730e330a1-810cfc05332f14cf.elb.eu-west-2.amazonaws.com:8088/contributor/validationPrepConfig/'
business_layer_local_endpoint = 'http://192.168.99.102:31447/contributor/validationPrepConfig/'


def run_data_prep(event, context):
    print('Event: ' + str(event))
    queue_data = event['Records'][0]['body']
    reference_data = queue_data.strip('\n')
    json_reference_data = json.loads(reference_data)

    print('Data from queue: ' + str(event))
    reference = json_reference_data['reference']
    period = json_reference_data['period']
    survey = json_reference_data['survey']
    bpmId = json_reference_data['bpmId']

    query_response = "{\"Error\": \"No data found\"}"
    query_vars = 'reference=' + reference + ';' + 'period=' + period + ';' + 'survey=' + survey + ';'
    call_to_business_layer = business_layer_endpoint + query_vars
    print('Call to Business Layer: ' + call_to_business_layer)

    try:
        query_response = requests.get(business_layer_endpoint + query_vars)
        print('Response: ' + str(query_response))
        print(query_response.text, "TEXT")
        print(query_response.content, "CONTENT")
        print(query_response.status_code, "STATUS CODE")
        #return(query_response.content)
    except:
        print("{\"Error\": \"Problem with call to Business Layer\"}")
        print('Response: ' + query_response)
        print(query_response.content, "CONTENT")
        print(query_response.text, "TEXT")
        print(query_response.status_code, "STATUS CODE")
        return(query_response.content)


    # Parse String output to JSON
    query_output = json.loads(query_response.content)
    print("Query output: " + str(query_output))
    validation_output = query_output['validation_config']

    # Call function to parse data and change keys
    parsed_validation_config = parse_validation_data(validation_output)
    print("Parsed Validation Data : " + str(parsed_validation_config))

    # Extract response and contributor data

    # Combine all data together
