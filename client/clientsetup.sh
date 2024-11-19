#!/bin/bash
# Client setup script

# Create Docker volume
docker volume create clientvol

# Start container with server's address and port
docker-compose run -d client python client.py --server-url http://server:5000
