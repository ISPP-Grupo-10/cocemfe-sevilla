from django import forms
from .models import Document
from professionals.models import Professional

class PDFUploadForm(forms.ModelForm):
    professionals = forms.ModelMultipleChoiceField(
        queryset=Professional.objects.filter(is_superuser=False),
        widget=forms.CheckboxSelectMultiple,
        required=False  # Permite que no se seleccione ningún profesional
    )

    class Meta:
        model = Document
        fields = ['name', 'pdf_file', 'suggestion_end_date', 'ubication', 'professionals']
        widgets = {
            'suggestion_end_date': forms.DateInput(attrs={'type': 'date'})
        }