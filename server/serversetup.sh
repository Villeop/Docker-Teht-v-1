#!/bin/bash
# Server setup script

# Create Docker volume for server container
docker volume create servervol

# Create network for the app
docker network create app-network

# Start the server container
docker-compose up -d server
