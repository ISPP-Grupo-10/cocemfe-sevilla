import random
import string
from django import forms
from django.contrib.auth import get_user_model
from organizations.models import Organization
from .models import Professional

class ProfessionalForm(forms.ModelForm):
    class Meta:
        model = Professional
        fields = ['username', 'first_name', 'last_name', 'password', 'telephone_number', 'license_number', 'organizations', 'email', 'profile_picture']
    profile_picture = forms.ImageField(required=False)
    def __init__(self, *args, **kwargs):
        user_is_staff = kwargs.pop('user_is_staff', True)
        super(ProfessionalForm, self).__init__(*args, **kwargs)

        if not user_is_staff:
            self.fields.pop('username')
            self.fields.pop('first_name')
            self.fields.pop('last_name')
            self.fields.pop('license_number')
            self.fields.pop('organizations')
            self.fields.pop('profile_picture')
    
class ProfessionalCreationForm(forms.ModelForm):
    class Meta:
        model = Professional
        fields = ['username', 'first_name', 'last_name', 'email']

    telephone_number = forms.CharField(max_length=9, validators=[Professional.phone_number_validator])
    license_number = forms.CharField(max_length=20)
    organizations = forms.ModelChoiceField(queryset=Organization.objects.all())
    profile_picture = forms.ImageField(required=False)

    def save(self, commit=True):
        professional = super().save(commit=False)

        # Generar una contraseña aleatoria
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        professional.set_password(password)

        if commit:
            professional.save()

        return professional

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data