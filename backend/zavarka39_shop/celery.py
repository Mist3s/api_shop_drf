"""Settings celery."""
import os

from celery import Celery

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'zavarka39_shop.settings'
)
app = Celery('zavarka39_shop')
app.config_from_object(
    'django.conf:settings',
    namespace='CELERY'
)
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    """Debug task."""
    print(f'Request: {self.request!r}')
