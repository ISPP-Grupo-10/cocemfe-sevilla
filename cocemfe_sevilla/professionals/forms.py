from django import forms
from .models import Professional, Request

class ProfessionalForm(forms.ModelForm):
    class Meta:
        model = Professional
        fields = ['username','first_name', 'last_name', 'telephone_number', 'license_number', 'organizations', 'email', 'profile_picture']


    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    
class RequestCreateForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['email', 'description']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    
class RequestUpdateForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['status']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data