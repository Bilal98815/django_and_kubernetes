FROM python:3.10-slim

# FROM base as node_setup
RUN apt-get update && \
apt-get install -y curl netcat-openbsd && \
curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
apt-get install -y nodejs && \
apt-get clean && rm -rf /var/lib/apt/lists/*

RUN groupadd -g 1000 appgroup && \
useradd -m -u 1000 -g 1000 -s /bin/bash appuser

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN chown -R appuser:appgroup /app

COPY poetry.lock pyproject.toml ./

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

COPY --chown=appuser:appgroup . /app

COPY scripts /scripts

RUN chmod +x /scripts/entrypoint.sh

RUN poetry install

ARG GIT_COMMIT_SHA="xxxxxxx"
ENV GIT_COMMIT_SHA=${GIT_COMMIT_SHA}