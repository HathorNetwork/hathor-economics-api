
region = us-east-1

.PHONY: all
all: deploy-status deploy-total-supply

# Example: make deploy-status env-dir=venv/lib/python3.6/site-packages/
.PHONY: deploy-status
deploy-status:
	echo $(env-dir)
	cd $(env-dir)
	zip -r9 ${OLDPWD}/lambda.zip .
	cd ${OLDPWD}
	zip -g lambda.zip status.py
	aws lambda update-function-code --function-name status-economic --zip-file fileb://lambda.zip --region $(region)
	rm lambda.zip

.PHONY: deploy-total-supply
deploy-total-supply:
	zip -9 lambda.zip supply.py
	aws lambda update-function-code --function-name total-supply-economic --zip-file fileb://lambda.zip --region $(region)
	rm lambda.zip