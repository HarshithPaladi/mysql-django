# Stage 1
FROM python as builder
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /tmp
COPY requirements.txt ./requirements.txt
RUN python3 -m pip install --upgrade pip && python3 -m pip wheel --no-cache-dir --wheel-dir /tmp/wheels -r requirements.txt

# Stage 2
FROM python:3-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/
COPY --from=builder /tmp/ ./
COPY requirements.txt ./requirements.txt
RUN python3 -m pip install --no-index --find-links=/usr/src/wheels -r requirements.txt && rm -rf /usr/src/wheels
COPY . ./


