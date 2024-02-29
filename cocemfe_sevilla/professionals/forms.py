# forms.py

from django import forms
from .models import Professional

class ProfessionalForm(forms.ModelForm):
    class Meta:
        model = Professional
        fields = ['name', 'surname', 'telephone_number', 'license_number', 'organizations']
