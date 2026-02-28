from os import environ

from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['*']
SECRET_KEY = environ['SECRET_KEY']
