FROM ubuntu

# Install Python.
RUN apt-get update && apt-get install -y python python-dev python-pip python-virtualenv postgresql postgresql-contrib nginx

# establish working directories
ADD . /usr/src/app

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1

# install python packages 
ADD requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# Port to expose
EXPOSE 8000