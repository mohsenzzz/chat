FROM python:3.12-alpine

WORKDIR /chat


RUN apk update
RUN apk add  postgresql-dev

ADD requirements.txt /chat


RUN pip  install  -r requirements.txt
COPY . /chat


