import json

from typing import Any, Dict
from boto3 import client

from constants import base_payload, decimal_places

lambda_client = client('lambda', region_name='us-east-1')


def get_status_payload() -> Dict[str, Any]:
    """ Get payload data from status lambda function
    """
    invoke_response = lambda_client.invoke(FunctionName='status-economic')
    payload = json.loads(invoke_response['Payload'].read().decode('utf-8'))
    return payload


def total_supply(event: Dict[str, Any], context: 'bootstrap.LambdaContext') -> Dict[str, Any]:
    """ Return the total supply getting data from the status lambda function
    """
    status_payload = get_status_payload()
    if status_payload['statusCode'] != 200:
        # In case of error we return the same payload
        return status_payload

    payload = base_payload
    payload['body'] = status_payload['body']['total_supply']
    return payload


def circulating_supply(event: Dict[str, Any], context: 'bootstrap.LambdaContext') -> Dict[str, Any]:
    """ Return the circulating supply getting data from the status lambda function
    """
    status_payload = get_status_payload()
    if status_payload['statusCode'] != 200:
        # In case of error we return the same payload
        return status_payload

    circulating_supply = status_payload['body']['circulating_supply']
    if event.get('decimals'):
        # If we have decimals: true in the parameter, return as decimal
        circulating_supply /=  10**decimal_places

    payload = base_payload
    payload['body'] = circulating_supply
    return payload