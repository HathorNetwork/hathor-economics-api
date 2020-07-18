import json

from typing import Any, Dict

from constants import BASE_PAYLOAD
from util import get_economics_status, get_status_default_error


def run(event: Dict[str, Any], context: 'bootstrap.LambdaContext') -> Dict[str, Any]:
    """ Get mined tokens from the full node and return the economics status of the network
    """
    # Default for status with no decimals parameter is true
    decimals = True
    queryStringParams = event.get('queryStringParameters')
    if queryStringParams and queryStringParams.get('decimals') == 'false':
        decimals = False

    # Get mined tokens from full node
    # Status requests always format with thousands separator when returning decimals
    status = get_economics_status(decimals, True)
    if not status:
        # In case of error we return the default error
        return get_status_default_error()

    payload = BASE_PAYLOAD
    payload['body'] = json.dumps(status, indent=4).encode('utf-8')

    return payload
