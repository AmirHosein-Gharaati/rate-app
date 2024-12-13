FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Installing all python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY entrypoint.sh /app/entrypoint.sh

# Get the django project into the docker container
ADD ./ /app/

ENTRYPOINT ["/app/entrypoint.sh"]