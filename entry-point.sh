#!/usr/bin/env bash
set -e

if [[ -z "${PORT}" ]]; then
    export PORT=8080
fi

if [ "$1" == "migrate" ]; then
    exec python manage.py migrate
fi

if [ "$1" == "sync_roles" ]; then
    exec python manage.py all_tenants_command sync_roles --reset_user_permissions
fi

if [ "$1" == "tenant_sync_roles" ]; then
    shift
    exec python manage.py tenant_command sync_roles --reset_user_permissions --schema=$1
fi

if [ "$1" == "static" ]; then
    exec python manage.py collectstatic --verbosity 2 --noinput
fi

if [ "$1" == "shell" ]; then
    exec python manage.py shell
fi

if [ "$1" == "manage" ]; then
    # run arbitrary manage.py commands
    shift
    exec python manage.py "$@"
fi

if [ "$1" == "run" ]; then
    export OTEL_SERVICE_NAME=platform
    export OTEL_EXPORTER_OTLP_ENDPOINT="https://api.honeycomb.io"
    exec opentelemetry-instrument gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 -c gunicorn.config.py config.wsgi:application
fi
