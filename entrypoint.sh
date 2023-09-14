#!/bin/bash

set -e

sleep 10

# Create database and table
python3 countapp/init_database.py

# Run Application using app.py
# python3 countapp/app.py
gunicorn --bind 0.0.0.0:5000 --chdir countapp countapp.wsgi:app --reload --timeout=900