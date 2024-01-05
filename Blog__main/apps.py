from django.apps import AppConfig


class BlogMainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Blog__main'
    def ready(self):
        import Blog__main.signals
