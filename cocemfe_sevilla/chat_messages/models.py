from django.db import models
from documents.models import Document
from professionals.models import Professional
from django.core.exceptions import ValidationError

class ChatMessage(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='chat_messages')
    author = models.ForeignKey(Professional, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Mensaje de {self.author.username} en {self.document.name}'

    class Meta:
        db_table = 'chat_messages'

    def clean(self):
        super().clean()
        # Validación: Verificar que el campo 'content' no exceda una cierta longitud máxima.
        if len(self.content) > 500:
            raise ValidationError("El contenido del mensaje no puede exceder los 500 caracteres.")