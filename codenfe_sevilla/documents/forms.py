from django import forms
from .models import Document

class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'pdf_file', 'end_date']
        widgets = {
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }
