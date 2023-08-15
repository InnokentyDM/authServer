FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]
