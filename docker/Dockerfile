FROM python:3
LABEL authors="dkhorkov"

WORKDIR /app

COPY . /app

# Changing permissions for correct work inside docker:
RUN chmod +x /app/docker/entrypoint.sh

RUN pip install -r requirements.txt
