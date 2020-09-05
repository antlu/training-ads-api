FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/local/src/ads-api

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv \
    && pipenv install --system --dev --skip-lock

COPY . ./

RUN useradd --create-home --shell /bin/bash --no-user-group user \
    && chown -R user:users .

USER user
