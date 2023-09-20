#!/usr/bin/env bash

# exit on error
set -o errexit

# install dependencies
pip install -r dependencies.txt

# run migrations in case any migrations not run yet
python manage.py migrate

chmod a+x setup.sh