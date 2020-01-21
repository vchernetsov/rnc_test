"""Gunicorn config"""
from envparse import env


APP_HOST = env.str("APP_HOST")
APP_PORT = env.int("APP_PORT")
daemon = False
bind = f"{APP_HOST}:{APP_PORT}"
max_requests = 9999
max_requests_jitter = 100
workers = 10
reload = True
