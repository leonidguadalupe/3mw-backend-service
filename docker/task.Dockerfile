FROM python:3.7-alpine

ADD . /app
WORKDIR /app

RUN apk add --no-cache postgresql-libs \
    && apk add --no-cache --virtual .build-deps \
    alpine-sdk libffi-dev openssl-dev \
    gcc musl-dev postgresql-dev \
    && addgroup -S _uwsgi && adduser _uwsgi -G _uwsgi -D \
    && python3 -m pip install uwsgi poetry --no-cache-dir \
    && poetry config settings.virtualenvs.create false \
    && rm -rf /app/lib/*/pip-wheel-metadata .venv \
    && make \
    && apk --purge del .build-deps \
    && find / -type d -name __pycache__ -exec rm -r {} + \
    && rm -rf /root/.cache /var/cache

EXPOSE 8080