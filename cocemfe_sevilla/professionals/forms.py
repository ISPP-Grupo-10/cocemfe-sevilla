from django import forms
from .models import Professional

class ProfessionalForm(forms.ModelForm):
    class Meta:
        model = Professional
        fields = ['username','first_name', 'last_name', 'telephone_number', 'license_number', 'organizations', 'email', 'profile_picture']


    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data