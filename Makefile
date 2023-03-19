.PHONY: help clean-build clean-pyc clean install-% test get-version build-python-library
.DEFAULT_GOAL := help

# Useful constants
PACKAGE_VERSION ?= $(shell ./version.sh)


# Auto Doc
define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef

export PRINT_HELP_PYSCRIPT

help:
		@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean-build: ## Remove build artifacts
		rm -rf build dist .eggs .cache
		find . -name '*.egg-info' -exec rm -fr {} +
		find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## Remove Python file artifacts
		find . -name '*.pyc' -exec rm -f {} +
		find . -name '*.pyo' -exec rm -f {} +
		find . -name '*~' -exec rm -f {} +
		find . -name '__pycache__' -exec rm -fr {} +

clean: clean-build clean-pyc  ## Remove build and python artifacts

install-%: ## Installing Python Packages
		@pip install -r $*.txt

test: install-requirements_test  ## Uses pytest to test the tests/ folder
		pytest tests

get-version: ## Gets the version of the package
		@echo $(shell ./version.sh)

build-python-library: clean ## Build Python Package
		@python setup.py sdist bdist_wheel > /dev/null
