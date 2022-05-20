FROM python:alpine AS build-base

ENV TZ=Europe/Moscow

WORKDIR /src/

RUN apk add --no-cache \
    tzdata \
    postgresql-dev

COPY requirements.txt .
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    linux-headers \
    libffi-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del --no-cache .build-deps

COPY . .


FROM build-base AS build-development
RUN wget -qO /bin/wait-for https://raw.githubusercontent.com/eficode/wait-for/v2.1.3/wait-for && chmod +x /bin/wait-for
RUN pip install --no-cache-dir -r requirements.dev.txt
