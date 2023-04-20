#!/bin/bash

python manage.py makemigrations && python manage.py migrate

python manage.py loaddata fixtures/db.json

echo 'migrations executed'