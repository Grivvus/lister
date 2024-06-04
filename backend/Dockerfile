FROM python:3.12-bookworm

WORKDIR /app

RUN apt-get update  && apt-get install -y --no-install-recommends git
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

ENV PYTHONPATH=/app

COPY . /app/

RUN poetry install --no-root
