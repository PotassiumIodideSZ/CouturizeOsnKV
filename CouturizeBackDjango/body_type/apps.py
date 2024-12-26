from django.apps import AppConfig

class BodyTypeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'body_type'

    def ready(self):
        import body_type.signals
