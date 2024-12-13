#!/bin/sh

python manage.py flush --no-input

echo "Running migrations..."
python manage.py migrate

echo "Starting Django server..."
exec "$@"