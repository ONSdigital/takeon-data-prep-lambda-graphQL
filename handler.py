import json
from aws_queue import send_to_error_queue, send_to_wrangler_queue
from api_calls import build_data_endpoint_url, call_endpoint_to_get_validation_config


def run_data_prep(event, context):
    f'AWS source event: {event}'
    contributor_definition = extract_json_from_eventbody(event)
    api_datasource_endpoint = build_data_endpoint_url(contributor_definition)

    f'Calling validation data/config endpoint: {api_datasource_endpoint}'
    validation_config = call_endpoint_to_get_validation_config(api_datasource_endpoint)

    if validation_config is None:
        send_to_error_queue(f'Error loading validation config data using: {api_datasource_endpoint}')

    validation_config['bpmid'] = contributor_definition['bpmId']
    f'Validation config data to place on wrangler queue: {validation_config}'

    if send_to_wrangler_queue(validation_config) is None:
        send_to_error_queue(f'Error sending validation config to wrangler queue')


def extract_json_from_eventbody(aws_event):
    queue_data = aws_event['Records'][0]['body']
    reference_data = queue_data.strip('\n')
    return json.loads(reference_data)
