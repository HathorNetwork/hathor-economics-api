This repository has AWS lambda functions for the economics APIs.

## Available APIs

- **Status:** https://api.economics.hathor.network/status
- **Total supply:** https://api.economics.hathor.network/total-supply
- **Circulating supply:** https://api.economics.hathor.network/circulating-supply
- **Circulating supply decimal:** https://api.economics.hathor.network/circulating-supply?decimals=true

## Update released premined tokens

1. Update value `released_premined_tokens` at `constants.py`
2. Deploy new lambda code: `make deps all`

`make deps` exports the locked dependencies from `poetry.lock` and installs them into `build/deps`, built for the Lambda runtime (Python 3.13, x86_64). It needs [uv](https://docs.astral.sh/uv/). To change a dependency, edit `pyproject.toml` and run `poetry lock`.

## Runtime

The functions run on the `python3.13` Lambda runtime. The runtime is set on the functions, not in this repository. To change it, run `make update-runtime runtime=<runtime>`, then deploy code built for that runtime.