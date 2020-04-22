import datetime
import requests

from os import path
from typing import Any, Dict

from constants import base_payload, released_premined_tokens, server, total_premined


def run(event: Dict[str, Any], context: 'bootstrap.LambdaContext') -> Dict[str, Any]:
    """ Get mined tokens from the full node and return the economics status of the network
    """
    # Get mined tokens from full node
    response = requests.get(path.join(server, 'mined_tokens'))
    if response and response.status_code == 200:
        data = response.json()

        mined_tokens = data['mined_tokens']
        circulating_supply = mined_tokens + released_premined_tokens
        total_supply = mined_tokens + total_premined

        body = {
            'latest_update': int(datetime.datetime.now().timestamp()),
            'backend': server,
            'total_supply': total_supply,
            'circulating_supply': circulating_supply,
            'mined_tokens': mined_tokens,
            'released_premined_tokens': released_premined_tokens
        }
    else:
        # XXX Uncoment it when the full node starts responding properly
        #payload = base_payload
        #payload['body'] = 'Error getting data from the server.'
        #payload['statusCode'] = 503
        #return payload

        data = {'mined_tokens': 12345678}

        mined_tokens = data['mined_tokens']
        circulating_supply = mined_tokens + released_premined_tokens
        total_supply = mined_tokens + total_premined

        body = {
            'latest_update': int(datetime.datetime.now().timestamp()),
            'backend': server,
            'total_supply': total_supply,
            'circulating_supply': circulating_supply,
            'mined_tokens': mined_tokens,
            'released_premined_tokens': released_premined_tokens
        }

    payload = base_payload
    payload['body'] = body

    return payload
