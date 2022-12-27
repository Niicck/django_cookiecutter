#!/bin/bash

set -e

CURRENT_DIR=`dirname ${BASH_SOURCE[0]}`
ROOT_DIR=$CURRENT_DIR/../../..

python $ROOT_DIR/manage.py migrate

if [ "$DJANGO_CONFIGURATION" == "Local" ]; then
    python \
        -Xfrozen_modules=off \
        -m debugpy --listen 0.0.0.0:${DEBUGPY_PORT} \
        $ROOT_DIR/manage.py runserver ${DJANGO_HOST}:${DJANGO_PORT} \
        --insecure
else
    echo "TODO"
    # gunicorn --workers=1 --bind=${DJANGO_HOST}:${DJANGO_PORT} --chdir=$ROOT_DIR cookiecutter_niicck_django.wsgi:application
fi
