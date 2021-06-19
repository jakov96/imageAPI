FROM ubuntu:latest
LABEL maintainer="Yakov Sharygin <jasha3131@gmail.com>"

RUN apt-get update
RUN apt-get install -y nginx python3-pip && pip3 install uwsgi
RUN apt-get install -y python3-dev libpq-dev cron
RUN apt-get install -y unixodbc unixodbc-dev tdsodbc
RUN apt-get install -y nano

RUN apt-get install -y supervisor && rm -rf /var/lib/apt/lists/*
COPY configs/production/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ['python']
CMD ['app.py']
