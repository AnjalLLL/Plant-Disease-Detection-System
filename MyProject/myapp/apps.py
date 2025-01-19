from django.apps import AppConfig
from .utils import create_admin

def ready(self):
    create_admin()


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
