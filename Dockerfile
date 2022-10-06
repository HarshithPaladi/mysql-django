FROM python:3.10-slim-bullseye
WORKDIR /usr/src/
RUN apt-get update
RUN apt-get install -y default-libmysqlclient-dev build-essential
RUN python3 -m pip install --upgrade pip
COPY requirements.txt ./requirements.txt
RUN python3 -m pip install -r requirements.txt
COPY . ./
# RUN python3 manage.py migrate
# CMD [ "python3", "manage.py","migrate","&&","python3", "manage.py", "runserver", "0.0.0.0:8000"]
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
