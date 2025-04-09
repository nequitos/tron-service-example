
FROM debian:bullseye AS Linux

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y ca-certificates

FROM python:3.13.2-bullseye AS Python
ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /usr/tron-service-example
RUN echo "PATH=/usr/tron-service-example/src" > /etc/environment

# Building python dependent packages
COPY requirements.txt /usr/tron-service-example/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Сopy project to container
COPY src /usr/tron-service-example/src
COPY init_db.py /usr/tron-service-example