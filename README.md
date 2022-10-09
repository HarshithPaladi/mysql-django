# MySQL - Django Docker Compose Example
1. Download the docker-compose.yml from 
`
https://raw.githubusercontent.com/HarshithPaladi/mysql-django/beta/docker-compose.yml
`
> Use wget
1. Pull the image :
```
docker pull ghcr.io/harshithpaladi/mysql-django:master
```
1. Use Docker Compose to start the services
```
docker compose up -d
```