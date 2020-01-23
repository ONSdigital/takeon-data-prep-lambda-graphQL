import os
import requests
import json


def build_data_endpoint_url(contributor):
    query_variables = 'reference=' + contributor['reference'] + ';period=' + contributor['period'] + ';survey=' + contributor['survey'] + ';'
    business_layer_endpoint = os.getenv("BUSINESS_LAYER_ENDPOINT")
    return business_layer_endpoint + query_variables


def call_endpoint_to_get_validation_config(api_endpoint):
    try:
        query_response = requests.get(api_endpoint)
    except:
        f'Error: Problem with call to Business Layer'
        return None
    finally:
        f'Response: {query_response}'
        f'Content: {query_response.content}'
        f'Text: {query_response.text}'
        f'Status Code: {query_response.status_code}'
    return json.loads(query_response.content)
