from django.db import models
from django.contrib.auth.models import User
from documents.models import Document
from professionals.models import Professional


class ChatMessage(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='chat_messages')
    author = models.ForeignKey(Professional, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Mensaje de {self.author.username} en {self.document.name}'

    class Meta:
        db_table = 'chat_messages'
