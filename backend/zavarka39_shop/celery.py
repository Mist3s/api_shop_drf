import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_shop.settings')

app = Celery('django_shop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.conf.broker_connection_retry_on_startup = True
app.autodiscover_tasks()
