import datetime
import requests
import sys

from os import path
from typing import Any, Dict, Union

from constants import BASE_PAYLOAD, DECIMAL_PLACES, RELEASED_PREMINED_TOKENS, SERVER, TOTAL_PREMINED


def get_economics_status(decimals: bool, add_comma_separator: bool) -> Dict[str, Any]:
    """ Get economics status data
    """
    status = None
    # Get mined tokens from full node
    response = requests.get(path.join(SERVER, 'getmininginfo'))
    if response and response.status_code == 200 and response.json().get('success'):
        data = response.json()

        mined_tokens = data['mined_tokens']
        circulating_supply = mined_tokens + RELEASED_PREMINED_TOKENS
        total_supply = mined_tokens + TOTAL_PREMINED

        status = {
            'latest_update': int(datetime.datetime.now().timestamp()),
            'backend': SERVER,
            'total_supply': format_amount(total_supply, decimals, add_comma_separator),
            'circulating_supply': format_amount(circulating_supply, decimals, add_comma_separator),
            'mined_tokens': format_amount(mined_tokens, decimals, add_comma_separator),
            'released_premined_tokens': format_amount(RELEASED_PREMINED_TOKENS, decimals, add_comma_separator),
        }

    return status


def format_amount(value: int, decimals: bool, add_comma_separator: bool) -> Union[int, str]:
    if decimals:
        return get_decimals(value, add_comma_separator)
    else:
        return value


def get_decimals(value: int, add_comma_separator: bool) -> str:
    assert sys.version_info >= (3, 6)
    value /= 10**DECIMAL_PLACES
    # This fixes the case where the decimal places are .00, so we must return with all zeros
    if add_comma_separator:
        # Format with comma thousand separator
        string_formatter = '{:,.{}f}'
    else:
        # Format only the decimals
        string_formatter = '{:.{}f}'

    return string_formatter.format(value, DECIMAL_PLACES)


def get_status_default_error() -> Dict[str, Any]:
    """ Return a payload with the default error when getting status data
        This is the error when there was a problem getting mined tokens in the full node
    """
    payload = BASE_PAYLOAD
    payload['body'] = 'Error getting data from the server.'
    payload['statusCode'] = 503
    return payload