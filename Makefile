.PHONY: setup run
SHELL := /bin/bash
BASE_DIR := $(shell pwd)
PYTHONPATH=$(BASE_DIR)

# setup
setup:
	@echo "Setup environment..."
	export PYTHONPATH=$(BASE_DIR)
	poetry install
	echo PYTHONPATH: $(PYTHONPATH)

env-setup:
	@echo "Setup environment..."
	@bash -c 'export PYTHONPATH=$(BASE_DIR) && \
	set -a && \
	source .env.dev && \
	set +a && \
	echo PYTHONPATH: $(PYTHONPATH) && \
	echo TEST_ENV: $$TEST_ENV'

test-unit:
	@echo "Running backend unit tests..."
	export PYTHONPATH=$(BASE_DIR)
	poetry run pytest -m unit 
