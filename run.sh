#!/bin/bash

# Build the images
docker-compose build

# Run the containers
docker-compose up -d