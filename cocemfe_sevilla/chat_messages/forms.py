from django import forms
from .models import ChatMessage

class MessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['content']
