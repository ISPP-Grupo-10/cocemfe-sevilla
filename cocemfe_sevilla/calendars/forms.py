from django import forms
from .models import Events

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['title', 'description', 'datetime', 'document', 'type']  
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'type': forms.Select(attrs={'class': 'form-control'})
        }