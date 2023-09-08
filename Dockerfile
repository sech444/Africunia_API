# pull official base image
FROM python:3.12.0rc1

# set work directory
WORKDIR /usr/Africunia_API/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY ./requirements.txt /usr/new_app/requirements.txt

# install dependencies
#RUN set -eux \
#   && apt-get add --no-cache --virtual .build-deps build-base \
#        libressl-dev libffi-dev gcc musl-dev python3-dev \
#    && pip install --upgrade pip setuptools wheel \
#   && pip install -r /usr/Africunia_API/app/requirements.txt \
#    && rm -rf /root/.cache/pip

RUN apt-get update -y \
    && apt-get install -y gcc libpq-dev \
    && /usr/local/bin/python -m pip install --upgrade pip \
    && pip3 install -r /usr/new_app/requirements.txt --no-cache-dir


# copy project
COPY . /usr/Africunia_API/


CMD ["uvicorn", "app.main:app", "--workers 4", "--host 0.0.0.0", "--port", "80"]