#!/bin/sh

if [ "$FLASK_ENV" = "development" ]
then
    echo "Creating the database tables..."
    python manage.py create_db
    python manage.py seed_db
    echo "Tables created"
fi

exec "$@"