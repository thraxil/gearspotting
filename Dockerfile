FROM python:3.10-slim@sha256:621488956f7e14ca249420e37dbecd59f669a8776bef0429aa89a4ebd8c6de9e
RUN apt-get update \
    && apt-get -y install libpq-dev gcc python3-dev

ENV APP_HOME /app
WORKDIR $APP_HOME

ENV PYTHONUNBUFFERED 1
EXPOSE 8000
ENV APP gearspotting

COPY requirements.txt .
RUN pip install --no-deps --no-cache-dir -r requirements.txt

COPY . .
ENV DJANGO_SETTINGS_MODULE gearspotting.settings_docker
ENV COMPRESS true
RUN python manage.py collectstatic --verbosity 2 --noinput
ENTRYPOINT ["/usr/bin/env", "bash", "/app/entry-point.sh"]
CMD ["run"]
