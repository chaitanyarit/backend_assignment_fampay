# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /youtube_api_fampay

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV YARL_NO_EXTENSIONS=1
ENV MULTIDICT_NO_EXTENSIONS=1

RUN apk add gcc python3-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate