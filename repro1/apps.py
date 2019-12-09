from django.apps import AppConfig


class Repro1Config(AppConfig):
    name = 'repro1'

    def ready(self):
        import repro1.signals