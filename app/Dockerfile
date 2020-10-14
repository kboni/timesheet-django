FROM python:3.8.5

ARG ENVIRONMENT

RUN mkdir -p /usr/removir/timesheet

WORKDIR /usr/removir/timesheet

COPY . /usr/removir/timesheet/

RUN pip install -r requirements/${ENVIRONMENT}.txt

