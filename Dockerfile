FROM python:3.12.1

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8

ADD . /api
WORKDIR /api

RUN apt-get update -y && apt-get upgrade -y 

RUN pip install --upgrade pip
RUN pip install -r requirements.txt