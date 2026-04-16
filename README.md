# Stage 1 - Build & Deploy a Personal API

A minimal FastAPI application for the HNG DevOps Stage 1 task. The API exposes three JSON endpoints and is intended to be deployed on a Linux VPS behind an Nginx reverse proxy.

## Project Overview

This project provides the following endpoints:

- `GET /` returns `{"message": "API is running"}`
- `GET /health` returns `{"message": "healthy"}`
- `GET /me` returns personal details in JSON format

The application runs on a private local port on the server, while Nginx handles public traffic and forwards requests to the app.

## Live URL

Base URL: `https://hnginfra.duckdns.org`

Update this value with your deployed domain or public server IP.

## Endpoints

### `GET /`

Returns:

```json
{
  "message": "API is running"
}
```

### `GET /health`

Returns:

```json
{
  "message": "healthy"
}
```

### `GET /me`

Returns:

```json
{
  "name": "Daniel Ogbuti",
  "email": "danielogbuti@gmail.com",
  "github": "https://github.com/dahnny"
}
```

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Nginx
- Linux VPS
- systemd

## Local Development

### Prerequisites

- Python 3.10+
- pip

### Setup

```bash
git clone https://github.com/dahnny/hnginternship.git
cd hnginternship

python3 -m venv .venv
source .venv/bin/activate

pip install fastapi uvicorn
```

### Run Locally

```bash
uvicorn main:app --reload
```

The app will be available at `http://127.0.0.1:8000`.

## Deployment

The application can be deployed on a Linux VPS and managed with `systemd`.
Nginx sits in front of the FastAPI process and forwards public traffic to the app running on a private port.

### Deployment Flow

1. The FastAPI app runs on `127.0.0.1:8000`.
2. Nginx listens on the public domain or IP address.
3. Nginx forwards incoming requests to the FastAPI app.
4. `systemd` keeps the service running automatically.

## Service Management

Useful commands:

```bash
sudo systemctl status api
sudo systemctl restart api
sudo systemctl enable api
```

## Author

- Name: Daniel Ogbuti
- Email: danielogbuti@gmail.com
- GitHub: https://github.com/dahnny