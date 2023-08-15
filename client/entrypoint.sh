#!/bin/sh

# Function to check if a service is up using curl
wait_for_service() {
    url="$1"
    retries=5
    wait_time=3

    while [ $retries -gt 0 ]; do
        response=$(curl --write-out '%{http_code}' --silent --output /dev/null "$url")
        if [ "$response" -eq 200 ]; then
            # If we get a 200 response, the service is up
            break
        else
            retries=$((retries-1))
            echo "Waiting for $url to return 200 OK. Retries left: $retries"
            sleep $wait_time
        fi
    done

    if [ $retries -le 0 ]; then
        echo "Error: $url did not return 200 OK after multiple attempts"
        exit 1
    fi
}

# Wait for auth and resource_api services to return 200 OK on their /health endpoints
wait_for_service http://auth:8000/health
wait_for_service http://resource_api:8000/health

# Run the main.py
exec python main.py
