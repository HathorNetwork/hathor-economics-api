import json

from typing import Any, Dict

from constants import base_payload, decimal_places
from util import get_economics_status, get_status_default_error


def total_supply(event: Dict[str, Any], context: 'bootstrap.LambdaContext') -> Dict[str, Any]:
    """ Return the total supply getting data from the status lambda function
    """
    status = get_economics_status()
    if not status:
        # In case of error we return the default error
        return get_status_default_error()

    payload = base_payload
    payload['body'] = status['total_supply']
    return payload


def circulating_supply(event: Dict[str, Any], context: 'bootstrap.LambdaContext') -> Dict[str, Any]:
    """ Return the circulating supply getting data from the status lambda function
    """
    status = get_economics_status()
    if not status:
        # In case of error we return the default error
        return get_status_default_error()

    circulating_supply = status['circulating_supply']
    queryStringParams = event.get('queryStringParameters')
    if queryStringParams and queryStringParams.get('decimals') == 'true':
        # If we have decimals: true in the parameter, return as decimal
        circulating_supply /=  10**decimal_places

    payload = base_payload
    payload['body'] = circulating_supply
    return payload