APP_NAME = "sse_script"

.PHONY: install test

default: run

install:
	pipenv install --dev --skip-lock

run-mongo:
	docker run -d -p 27017:27017 mongo:latest

test:
	PYTHONPATH=./src/sse_script pytest --verbose

run:
	bash start.sh
