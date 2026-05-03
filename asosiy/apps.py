from django.apps import AppConfig


class AsosiyConfig(AppConfig):
    name = 'asosiy'
    def ready(self):
        import asosiy.signals
