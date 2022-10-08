#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

python manage.py createsuperuser
jpcortesg
jpcortesg@hotmail.com
jpcortesg123.
jpcortesg123.