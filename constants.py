# Full node server URL to connect to
server = 'https://node1.mainnet.hathor.network/v1a/'

# Number of decimal places
decimal_places = 2

# Quantity of tokens already released from the premine
# Value is an integer
# 20M tokens released * 10**2 for the decimal valiue
released_premined_tokens = 20 * 10**6 * 10**decimal_places

# Premined tokens
# Value is an integer
# 1B tokens premined * 10**2 for the decimal value
total_premined = 1 * 10**9 * 10**decimal_places

# Payload base for a success message of return for API gateway
# Methods just need to fill the 'body'
base_payload = {
    "isBase64Encoded": True,
    "statusCode": 200,
    "headers": {},
}
