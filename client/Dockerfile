FROM python:3.9-slim

WORKDIR /app

COPY client.py .

RUN pip install requests

# Create the clientdata volume directory
RUN mkdir -p /clientdata

# Define the volume
VOLUME /clientdata

# Run the client app
CMD ["python", "client.py"]
