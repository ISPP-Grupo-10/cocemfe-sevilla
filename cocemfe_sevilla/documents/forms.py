from django import forms
from .models import Document
from professionals.models import Professional

class PDFUploadForm(forms.ModelForm):

    professionals = forms.ModelMultipleChoiceField(queryset=Professional.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Document
        fields = ['name', 'pdf_file', 'end_date','ubication', 'professionals']
        widgets = {
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }
