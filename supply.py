import json
import sys

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

    payload = BASE_PAYLOAD

    circulating_supply = status['circulating_supply']
    payload['body'] = circulating_supply

    queryStringParams = event.get('queryStringParameters')
    if queryStringParams and queryStringParams.get('decimals') == 'true':
        assert sys.version_info >= (3, 6)
        # If we have decimals: true in the parameter, return as decimal
        circulating_supply /=  10**DECIMAL_PLACES
        # This fixes the case where the decimal places are .00, so we must return with all zeros
        circulating_supply_str = '%.{}f'.format(DECIMAL_PLACES) % circulating_supply
        payload['body'] = circulating_supply_str

    return payload