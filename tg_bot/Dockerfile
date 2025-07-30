FROM python:3.13-slim-bookworm

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends git curl
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONPATH=/app

COPY pyproject.toml /app/
COPY uv.lock /app/

RUN uv pip install \
    --system \
    --no-cache \
    --requirement /app/pyproject.toml

COPY . /app/
