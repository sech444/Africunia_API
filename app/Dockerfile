# pull official base image
FROM python:3.9.2

# set work directory
WORKDIR /usr/Africunia_API/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY ./requirements.txt /usr/Africunia_API/app/requirements.txt

# install dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /usr/Africunia_API/app/requirements.txt \
    && rm -rf /root/.cache/pip

# copy project
COPY . /usr/Africunia_API/app/
