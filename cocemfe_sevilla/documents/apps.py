from django.apps import AppConfig
import sys

class DocumentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'documents'

    def ready(self):
        if 'migrate' not in sys.argv and 'makemigrations' not in sys.argv:
            import documents.tasks