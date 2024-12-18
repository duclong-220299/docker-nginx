FROM python:3.10-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./src .
