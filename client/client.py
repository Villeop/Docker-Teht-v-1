import requests
import hashlib
import time
import argparse
import sys

# Getting the server-url from the docker-compose.yml
parser = argparse.ArgumentParser(description='Client for file transfer')
parser.add_argument('--server-url', type=str, required=True, help='URL of the server')
args = parser.parse_args()

server_url = args.server_url

# Wait for the server
for _ in range(10):
    try:
        # Get file from server
        file_response = requests.get(f'{server_url}/file')
        file_response.raise_for_status()
        break
    except requests.exceptions.RequestException as e:
        print(f"Server not ready, retrying in 5 seconds... ({e})")
        sys.stdout.flush()
        time.sleep(5)
else:
    print("Failed to connect to the server.")
    sys.stdout.flush()
    exit(1)

file_content = file_response.text

# Save file to /clientdata
with open('/clientdata/random.txt', 'w') as f:
    f.write(file_content)

# Get checksum from server
checksum_response = requests.get(f'{server_url}/checksum')
server_checksum = checksum_response.text.strip()

# Calculate local checksum
local_checksum = hashlib.md5(file_content.encode()).hexdigest()

# Verify checksum
if local_checksum == server_checksum:
    print("File transfer successful and checksum verified.")
else:
    print("Checksum verification failed.")
sys.stdout.flush()

# Keep the container running
while True:
    time.sleep(60)
