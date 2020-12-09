FROM python:3.8.6-alpine

LABEL maintainer James Neyer "james@neyer.net"

ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

CMD flask run --host 0.0.0.0