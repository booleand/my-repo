NAME=deploy-ml-api
AWS_NAME=ml-api
COMMIT_ID=$(shell git rev-parse HEAD)

build-ml-api-heroku:
	docker build --build-arg PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} -t registry.heroku.com/$(NAME)/web:latest .

push-ml-api-heroku:
	docker push registry.heroku.com/${HEROKU_APP_NAME}/web:latest

build-ml-api-aws:
	docker build --build-arg PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} -t $(AWS_NAME):$(COMMIT_ID) .

push-ml-api-aws:
	docker push ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/$(AWS_NAME):$(COMMIT_ID)

tag-ml-api:
	docker tag $(AWS_NAME):$(COMMIT_ID) ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/$(AWS_NAME):$(COMMIT_ID)
