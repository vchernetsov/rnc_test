#!/bin/bash
echo "RUNNING ENVIRONMENT: $ENVIRONMENT"
gunicorn --config ./gunicorn_config.py settings.wsgi:application
