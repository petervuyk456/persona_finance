#!/bin/sh

if [ "$FLASK_ENV" = "development" ]
then
    python manage.py run_tests
    python manage.py create_collections
fi

exec "$@"