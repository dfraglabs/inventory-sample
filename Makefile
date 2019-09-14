BIN             = inventory
OUTPUT_DIR      = build
TMP_DIR        := .tmp
RELEASE_TIME   := $(shell date -u '+%Y-%m-%d_%I:%M:%S%p')
RELEASE_VER    := $(shell git rev-parse --short HEAD)
LDFLAGS        := "-s -w -X main.version=$(RELEASE_VER)-$(RELEASE_TIME)"
DOCKER_IP       = $(shell docker info | grep -q moby && echo localhost || docker-machine ip)
NAME            = default
COVERMODE       = atomic

.PHONY: help docs
.DEFAULT_GOAL := help

run: ## Run application (without building)
	python manage.py runserver

all: test build docker ## Test, build and docker image build

setup: installtools ## Install and setup tools


## Run Tests ##

test:

installtools: ## Install development related tools

## Migrations ##

migrations: migrations/make

migrations/make:
	python manage.py makemigrations

migrations/run:
	python manage.py migrate


## Build ##

build: ## build the app

docker: ## build docker image

docker/local:  ## Bring up the service via docker-compose
	docker-compose build
	docker stop $(BIN); docker rm $(BIN); docker-compose up

help: ## Display this help message
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_\/-]+:.*?## / {printf "\033[34m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | \
		sort | \
		grep -v '#'
