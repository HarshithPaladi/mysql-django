# Stage 1
FROM python:latest as builder
# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1
WORKDIR /tmp/pip
COPY requirements.txt ./requirements.txt
# RUN python3 -m pip install --upgrade pip && python3 -m pip wheel --no-cache-dir --wheel-dir /tmp/wheels -r requirements.txt
# Installing required packages into a folder to use them in later stage
RUN python3 -m pip install --no-cache-dir --target /tmp/pip -r requirements.txt

# Stage 2
# Using lightweight python image (alpine)
FROM python:3-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/
# Copying required packages from previous stage
COPY --from=builder /tmp/pip ./pip
# Adjusting the path to use the packages
ENV PYTHONPATH="${PYTHONPATH}:/usr/src/pip"
# Installing required packages for alpine image
RUN apk add --no-cache mariadb-connector-c
COPY . ./


