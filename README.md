This repository has AWS lambda functions for the economics APIs.

## Available APIs

- **Status:** https://api.economics.hathor.network/status
- **Total supply:** https://api.economics.hathor.network/total-supply
- **Circulating supply:** https://api.economics.hathor.network/circulating-supply
- **Circulating supply decimal:** https://api.economics.hathor.network/circulating-supply?decimals=true

## Update released premined tokens

1. Update value `released_premined_tokens` at `constants.py`
2. Deploy new lambda code: `make env_dir=env_dir`