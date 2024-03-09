from django import forms
from .models import Document
from professionals.models import Professional

class PDFUploadForm(forms.ModelForm):
    professionals = forms.ModelMultipleChoiceField(
        queryset=Professional.objects.filter(is_superuser=False),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Document
        fields = ['name', 'ubication', 'end_date', 'pdf_file', 'professionals', 'status'] 
        widgets = {
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(choices=Document.STATUS),
        }
