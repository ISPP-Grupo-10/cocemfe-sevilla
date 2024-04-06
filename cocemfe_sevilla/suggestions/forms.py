from django import forms
from .models import Suggestion
from professionals.models import Professional
from documents.models import Document

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['main', 'justification', 'relevance', 'section', 'page', 'date', 'professional', 'document']