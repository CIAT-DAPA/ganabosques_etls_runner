FROM python:3.11-slim

WORKDIR /runner

RUN apt-get update && apt-get install -y \
    git \
    gcc \
    g++ \
    build-essential \
    gdal-bin \
    libgdal-dev \
    libproj-dev \
    libgeos-dev \
 && rm -rf /var/lib/apt/lists/*

RUN pip install PyYAML

COPY repos.yml .
COPY clone_repositories.py .
COPY install_requirements.py .
COPY launcher.py .

RUN printf '#!/bin/sh\npython /runner/launcher.py "$@"\n' \
    > /usr/local/bin/etl \
    && chmod +x /usr/local/bin/etl

ARG GITHUB_TOKEN
ENV GITHUB_TOKEN=${GITHUB_TOKEN}

RUN python clone_repositories.py
RUN python install_requirements.py

ENTRYPOINT ["tail", "-f", "/dev/null"]