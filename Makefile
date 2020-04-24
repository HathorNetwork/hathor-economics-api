
region = us-east-1
current_dir = $(shell pwd)
lambda_zip = $(current_dir)/lambda.zip

.PHONY: all
all: deploy-status deploy-total-supply deploy-circulating-supply

# Example: make deploy-status env_dir=venv/lib/python3.6/site-packages/
.PHONY: deploy-status
deploy-status:
	echo $(env_dir)
	cd $(env_dir); zip -r9 $(lambda_zip) .
	zip -g lambda.zip status.py constants.py util.py
	aws lambda update-function-code --function-name status-economic --zip-file fileb://lambda.zip --region $(region)
	rm lambda.zip

# Example: make deploy-total-supply env_dir=venv/lib/python3.6/site-packages/
.PHONY: deploy-total-supply
deploy-total-supply:
	echo $(env_dir)
	cd $(env_dir); zip -r9 $(lambda_zip) .
	zip -g lambda.zip status.py constants.py util.py supply.py
	aws lambda update-function-code --function-name total-supply-economic --zip-file fileb://lambda.zip --region $(region)
	rm lambda.zip

# Example: make deploy-circulating-supply env_dir=venv/lib/python3.6/site-packages/
.PHONY: deploy-circulating-supply
deploy-circulating-supply:
	echo $(env_dir)
	cd $(env_dir); zip -r9 $(lambda_zip) .
	zip -g lambda.zip status.py constants.py util.py supply.py
	aws lambda update-function-code --function-name circulating-supply-economic --zip-file fileb://lambda.zip --region $(region)
	rm lambda.zip