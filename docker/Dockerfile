FROM python:3.10

ENV PYTHONUNBUFFERED 1

# Installing all python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Get the django project into the docker container
RUN mkdir /app
WORKDIR /app
ADD ./ /app/