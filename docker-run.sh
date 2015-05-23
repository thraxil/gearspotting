#!/bin/bash

cd /var/www/gearspotting/gearspotting/
python manage.py migrate --noinput --settings=gearspotting.settings_docker
python manage.py collectstatic --noinput --settings=gearspotting.settings_docker
python manage.py compress --settings=gearspotting.settings_docker
exec gunicorn --env \
  DJANGO_SETTINGS_MODULE=gearspotting.settings_docker \
  gearspotting.wsgi:application -b 0.0.0.0:8000 -w 3 \
  --access-logfile=- --error-logfile=-
