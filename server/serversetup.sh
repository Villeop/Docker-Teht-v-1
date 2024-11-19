#!/bin/bash
# Server setup script

# Create Docker volume
docker volume create servervol

# Create the network for the app
docker network create app-network

# Start the server container
docker-compose up -d server
