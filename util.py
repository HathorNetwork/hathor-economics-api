import datetime
import requests

from os import path
from typing import Any, Dict

from constants import base_payload, released_premined_tokens, server, total_premined


def get_economics_status() -> Dict[str, Any]:
    """ Get economics status data
    """
    status = None
    # Get mined tokens from full node
    response = requests.get(path.join(server, 'getmininginfo'))
    if response and response.status_code == 200 and response.json().get('success'):
        data = response.json()

        # XXX After the full node is updated to the new version, uncoment the line below
        #mined_tokens = data['mined_tokens']
        mined_tokens = 123456
        circulating_supply = mined_tokens + released_premined_tokens
        total_supply = mined_tokens + total_premined

        status = {
            'latest_update': int(datetime.datetime.now().timestamp()),
            'backend': server,
            'total_supply': total_supply,
            'circulating_supply': circulating_supply,
            'mined_tokens': mined_tokens,
            'released_premined_tokens': released_premined_tokens
        }

    return status


def get_status_default_error() -> Dict[str, Any]:
    """ Return a payload with the default error when getting status data
        This is the error when there was a problem getting mined tokens in the full node
    """
    payload = base_payload
    payload['body'] = 'Error getting data from the server.'
    payload['statusCode'] = 503
    return payload