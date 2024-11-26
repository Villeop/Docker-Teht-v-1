#!/bin/bash
# Client setup script

# URL and Port variables
SERVER_URL=$1
SERVER_PORT=$2

# Create Docker volume for client container
docker volume create clientvol

# Start the client container with the specified server URL and port
docker-compose run -d client python client.py --server-url "http://$SERVER_URL:$SERVER_PORT"
