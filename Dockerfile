# Dockerfile

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*


COPY src/requirements/base.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./src /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]