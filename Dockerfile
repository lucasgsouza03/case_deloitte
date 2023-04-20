FROM python:latest

ARG ENVIRONMENT

RUN python -m venv /env
ENV PATH /env/bin:$PATH

RUN pip install -U pip

ADD requirements.txt /app/requirements.txt
RUN /env/bin/pip install -r /app/requirements.txt
ADD . /app

ADD  .env /app/.env

WORKDIR /app

RUN mkdir "/app/static"

RUN python manage.py collectstatic

CMD gunicorn --max-requests 1000 --max-requests-jitter 50 -b :8000 case_deloitte.wsgi -w 4 --timeout 3600
