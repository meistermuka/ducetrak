SHELL=/bin/bash -o pipefail

init:
	pip3 install -r requirements.txt

init-dev: init
	pip3 install -r requirements-dev.txt

lint:
	flake8 app.py chalicelib/ tests/

test:
	pytest tests/