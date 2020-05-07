import json
import sys

from typing import Any, Dict

from constants import BASE_PAYLOAD, DECIMAL_PLACES
from util import get_economics_status, get_status_default_error


def get_payload(key: str, event: Dict[str, Any]) -> Dict[str, Any]:
    """ Return the payload for the request depending on the key (total_supply or circulating_supply)
    """
    status = get_economics_status()
    if not status:
        # In case of error we return the default error
        return get_status_default_error()

    payload = BASE_PAYLOAD

    value = status.get(key)
    assert value is not None

    payload['body'] = value

    queryStringParams = event.get('queryStringParameters')
    if queryStringParams and queryStringParams.get('decimals') == 'true':
        assert sys.version_info >= (3, 6)
        # If we have decimals: true in the parameter, return as decimal
        value /=  10**DECIMAL_PLACES
        # This fixes the case where the decimal places are .00, so we must return with all zeros
        value_str = '%.{}f'.format(DECIMAL_PLACES) % value
        payload['body'] = value_str

    return payload


def total_supply(event: Dict[str, Any], context: 'bootstrap.LambdaContext') -> Dict[str, Any]:
    """ Return the total supply getting data from the status lambda function
    """
    return get_payload('total_supply', event)


def circulating_supply(event: Dict[str, Any], context: 'bootstrap.LambdaContext') -> Dict[str, Any]:
    """ Return the circulating supply getting data from the status lambda function
    """
    return get_payload('circulating_supply', event)