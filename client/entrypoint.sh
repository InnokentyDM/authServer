#!/bin/sh

# Function to check if a service is up
wait_for_service() {
    host="$1"
    port="$2"

    while ! nc -z "$host" "$port"; do
        echo "Waiting for $host:$port..."
        sleep 1
    done
}

# Wait for auth and resource_api services
wait_for_service auth 8000
wait_for_service resource_api 8000

# Run the main.py
exec python main.py
