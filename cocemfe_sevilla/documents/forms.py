from django import forms
from .models import Document
from professionals.models import Professional

class PDFUploadForm(forms.ModelForm):

    pdf_file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True, 'accept': '.pdf'})
    )

    professionals = forms.ModelMultipleChoiceField(
        queryset=Professional.objects.filter(is_superuser=False),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Document
        fields = ['name', 'pdf_file','suggestion_start_date','suggestion_end_date','voting_end_date', 'ubication', 'professionals']
        widgets = {
            'suggestion_start_date': forms.DateInput(attrs={'type': 'date'}),
            'suggestion_end_date': forms.DateInput(attrs={'type': 'date'}),
            'voting_end_date': forms.DateInput(attrs={'type': 'date'}),
        }

