from django.apps import AppConfig
from threading import Thread

class RotinasAutomaticasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rotinas_automaticas'
    def ready(self):
       from .routines import configura_rotinas
       Thread(target=configura_rotinas).start()
