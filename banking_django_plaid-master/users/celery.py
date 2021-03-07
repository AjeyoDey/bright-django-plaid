from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banking_django_plaid.settings')
app = Celery('users', broker='redis://localhost:6379', backend='redis://localhost:6379')