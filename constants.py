# Full node server URL to connect to
SERVER = 'https://node1.mainnet.hathor.network/v1a/'

# Number of decimal places
DECIMAL_PLACES = 2

# Quantity of tokens already released from the premine
# Value is an integer
# Tokens released * 10**2 for the decimal valiue
RELEASED_PREMINED_TOKENS = 19740048 * 10**DECIMAL_PLACES

# Premined tokens
# Value is an integer
# 1B tokens premined * 10**2 for the decimal value
TOTAL_PREMINED = 1 * 10**9 * 10**DECIMAL_PLACES

# Payload base for a success message of return for API gateway
# Methods just need to fill the 'body'
BASE_PAYLOAD = {
    'isBase64Encoded': True,
    'statusCode': 200,
    'headers': {
        'Content-Type': 'text/plain',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
        'Access-Control-Allow-Methods': 'OPTIONS,GET'
    },
}
