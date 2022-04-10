FROM python:3.9.6

ENV PYTHONUNBUFFERED 1 

RUN mkdir /placementsbackend

WORKDIR /placementsbackend

ADD . /placementsbackend/

RUN touch /placementsbackend/.env

RUN pip install -r requirements.txt

# EXPOSE 8000

# CMD python manage.py runserver