FROM python:3.9-slim

WORKDIR /app

COPY server.py .

RUN pip install flask

# Create the serverdata volume directory
RUN mkdir -p /serverdata

# Define the volume
VOLUME /serverdata

# Run the server app
CMD ["python", "server.py"]
