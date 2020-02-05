import os
import requests
import json

def build_data_endpoint_url(contributor):
    query_variables = 'reference=' + contributor['reference'] + ';period=' + contributor['period'] + ';survey=' + contributor['survey'] + ';'
    business_layer_endpoint = os.getenv("BUSINESS_LAYER_ENDPOINT")
    return business_layer_endpoint + query_variables


def call_endpoint_to_get_validation_config(api_endpoint):
    try:
        response = requests.get(api_endpoint)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        error_response = {}
        error_response['error'] = f'Calling Business Layer: {err}'
        return error_response
    finally:
        print(f'Endpoint: {api_endpoint} - Status: {response.status_code} - Request time: {response.elapsed.total_seconds()}')

    return json.loads(response.content)
