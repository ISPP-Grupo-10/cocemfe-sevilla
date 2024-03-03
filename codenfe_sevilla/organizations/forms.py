# forms.py dentro de tu aplicación Django
from django import forms
from .models import Organization

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'telephone_number', 'address', 'email', 'zip_code']
        
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        telephone_number = cleaned_data.get('telephone_number')
        email = cleaned_data.get('email')
        
        if Organization.objects.filter(name=name).exists():
            self.add_error('name', "Este nombre ya está en uso.")
        
        if Organization.objects.filter(telephone_number=telephone_number).exists():
            self.add_error('telephone_number', "Este número de teléfono ya está en uso.")
        
        if Organization.objects.filter(email=email).exists():
            self.add_error('email', "Este email ya está en uso.")
        
        return cleaned_data
