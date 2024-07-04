#!/bin/bash

# Build the images
docker-compose build --parallel

# Run the containers
docker-compose up -d

# View running docker containers
docker ps