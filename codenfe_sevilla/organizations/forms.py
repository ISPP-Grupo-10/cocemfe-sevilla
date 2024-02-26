# forms.py dentro de tu aplicación Django
from django import forms
from .models import Organization

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'telephone_number', 'address', 'email', 'zip_code']
