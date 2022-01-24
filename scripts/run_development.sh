#!/usr/bin/env bash

# This script starts the development environment using Docker
# Launch as: source tools/run_development.sh from the project's root

DOCKER_COMPOSE_FILE="./docker-compose.yml"
SERVICE_NAME="pg_trunk"

CONTAINER_UID=$(id -u) CONTAINER_GID=$(id -g) docker-compose -f ${DOCKER_COMPOSE_FILE} stop
CONTAINER_UID=$(id -u) CONTAINER_GID=$(id -g) docker-compose -f ${DOCKER_COMPOSE_FILE} rm --force
CONTAINER_UID=$(id -u) CONTAINER_GID=$(id -g) docker-compose -f ${DOCKER_COMPOSE_FILE} up -d --remove-orphans --build
CONTAINER_UID=$(id -u) CONTAINER_GID=$(id -g) docker-compose -f ${DOCKER_COMPOSE_FILE} exec ${SERVICE_NAME} bash
