FROM python:3-alpine
MAINTAINER Edwin Matthijssen <edwin.matthijssen@tno.nl>

RUN apk add --update --no-cache g++ gcc libxslt-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

ENV PYTHONPATH=.:/usr/src/app

EXPOSE 4000

CMD cd /usr/src/app/application && python -u app.py