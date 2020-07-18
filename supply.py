import json

from typing import Any, Dict

from constants import BASE_PAYLOAD, DECIMAL_PLACES
from util import get_economics_status, get_status_default_error


def get_payload(key: str, event: Dict[str, Any]) -> Dict[str, Any]:
    """ Return the payload for the request depending on the key (total_supply or circulating_supply)
    """
    # For supply the default with no decimals parameter is false
    decimals = False
    queryStringParams = event.get('queryStringParameters')
    if queryStringParams and queryStringParams.get('decimals') == 'true':
        decimals = True

    # Supply requests never want to format thousand separator
    status = get_economics_status(decimals, False)
    if not status:
        # In case of error we return the default error
        return get_status_default_error()

    payload = BASE_PAYLOAD

    value = status.get(key)
    assert value is not None

    payload['body'] = value

    return payload


def total_supply(event: Dict[str, Any], context: 'bootstrap.LambdaContext') -> Dict[str, Any]:
    """ Return the total supply getting data from the status lambda function
    """
    return get_payload('total_supply', event)


def circulating_supply(event: Dict[str, Any], context: 'bootstrap.LambdaContext') -> Dict[str, Any]:
    """ Return the circulating supply getting data from the status lambda function
    """
    return get_payload('circulating_supply', event)