#!/bin/sh

set -e

echo "Application des migrations de la base de données..."

python manage.py migrate 

python manage.py collectstatic --no-input

exec "$@"