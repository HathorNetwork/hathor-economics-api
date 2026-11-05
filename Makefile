region = us-east-1
runtime = python3.13
current_dir = $(shell pwd)
lambda_zip = $(current_dir)/lambda.zip
build_dir = $(current_dir)/build
# Defaults to the clean dependency dir built by `make deps`.
env_dir ?= $(build_dir)/deps
functions = status-economic total-supply-economic circulating-supply-economic

.PHONY: all
all: deploy-status deploy-total-supply deploy-circulating-supply

# Install the runtime dependencies for the Lambda platform (Python 3.13, x86_64),
# whatever the local Python version is.
.PHONY: deps
deps:
	rm -rf $(build_dir)/deps
	pip install --quiet --target $(build_dir)/deps \
		--platform manylinux2014_x86_64 --implementation cp --python-version 3.13 \
		--only-binary=:all: -r requirements.txt

# One-time change of the runtime of all functions. Deploy code built for the same runtime.
.PHONY: update-runtime
update-runtime:
	for f in $(functions); do \
		aws lambda update-function-configuration --function-name $$f --runtime $(runtime) --region $(region) --query '[FunctionName,Runtime,LastUpdateStatus]' --output text && \
		aws lambda wait function-updated-v2 --function-name $$f --region $(region) || exit 1; \
	done

# Example: make deps deploy-status
.PHONY: deploy-status
deploy-status:
	echo $(env_dir)
	cd $(env_dir); zip -r9 $(lambda_zip) .
	zip -g lambda.zip status.py constants.py util.py
	aws lambda update-function-code --function-name status-economic --zip-file fileb://lambda.zip --region $(region)
	rm lambda.zip

# Example: make deps deploy-total-supply
.PHONY: deploy-total-supply
deploy-total-supply:
	echo $(env_dir)
	cd $(env_dir); zip -r9 $(lambda_zip) .
	zip -g lambda.zip status.py constants.py util.py supply.py
	aws lambda update-function-code --function-name total-supply-economic --zip-file fileb://lambda.zip --region $(region)
	rm lambda.zip

# Example: make deps deploy-circulating-supply
.PHONY: deploy-circulating-supply
deploy-circulating-supply:
	echo $(env_dir)
	cd $(env_dir); zip -r9 $(lambda_zip) .
	zip -g lambda.zip status.py constants.py util.py supply.py
	aws lambda update-function-code --function-name circulating-supply-economic --zip-file fileb://lambda.zip --region $(region)
	rm lambda.zip
