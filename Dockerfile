# syntax=docker/dockerfile:1
FROM python:slim
ENV PYTHONUNBUFFERED=1
WORKDIR /baseball_api
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY . .

