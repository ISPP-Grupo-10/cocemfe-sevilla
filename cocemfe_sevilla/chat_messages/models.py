from django.db import models
from documents.models import Document
from professionals.models import Professional
from django.core.exceptions import ValidationError
from django.utils import timezone

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
        
        # Validación: Verificar que la fecha de publicación del mensaje sea anterior a la fecha y hora actuales.
        if self.post_date > timezone.now():
            raise ValidationError("La fecha de publicación del mensaje no puede ser en el futuro.")
        
        # Validación: Verificar que los objetos relacionados existan en la base de datos.
        if not Professional.objects.filter(pk=self.author_id).exists():
            raise ValidationError("El autor especificado no existe.")
        if not Document.objects.filter(pk=self.document_id).exists():
            raise ValidationError("El documento especificado no existe.")