# Stage 1
FROM python as builder
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /tmp/pip
COPY requirements.txt ./requirements.txt
# RUN python3 -m pip install --upgrade pip && python3 -m pip wheel --no-cache-dir --wheel-dir /tmp/wheels -r requirements.txt
RUN python3 -m pip install --target /tmp/pip -r requirements.txt

# Stage 2
FROM python:3-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/
COPY --from=builder /tmp/pip ./pip
ENV PYTHONPATH="${PYTHONPATH}:/usr/src/pip"
RUN apk add --no-cache mariadb-connector-c
COPY . ./


