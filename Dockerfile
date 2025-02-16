FROM python:3.12-slim

COPY requirements.txt .
COPY requirements.dev.txt .

RUN pip --no-cache-dir install -U pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements.dev.txt

COPY . /app

WORKDIR /app
