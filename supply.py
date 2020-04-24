import json

from typing import Any, Dict

from constants import BASE_PAYLOAD, DECIMAL_PLACES
from util import get_economics_status, get_status_default_error


def total_supply(event: Dict[str, Any], context: 'bootstrap.LambdaContext') -> Dict[str, Any]:
    """ Return the total supply getting data from the status lambda function
    """
    status = get_economics_status()
    if not status:
        # In case of error we return the default error
        return get_status_default_error()

    payload = BASE_PAYLOAD
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
        circulating_supply /=  10**DECIMAL_PLACES

    payload = BASE_PAYLOAD
    payload['body'] = circulating_supply
    return payload