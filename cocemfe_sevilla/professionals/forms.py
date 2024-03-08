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

    def __init__(self, *args, **kwargs):
        user_is_staff = kwargs.pop('user_is_staff', True)
        super(ProfessionalForm, self).__init__(*args, **kwargs)

        if not user_is_staff:
            self.fields.pop('username', 'first_name', 'last_name', 'license_number', 'organizations', 'profile_picture')
    
class ProfessionalCreationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email']

    telephone_number = forms.CharField(max_length=9, validators=[Professional.phone_number_validator])
    license_number = forms.CharField(max_length=20)
    organizations = forms.ModelChoiceField(queryset=Organization.objects.all())
    profile_picture = forms.ImageField(required=False)

    def save(self, commit=True):
        user = super().save(commit=False)
        
        # Genera una contraseña aleatoria
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        user.set_password(password)

        if commit:
            user.save()

            professional = Professional.objects.create(
                user=user,
                telephone_number=self.cleaned_data['telephone_number'],
                license_number=self.cleaned_data['license_number'],
                organizations=self.cleaned_data['organizations'],
                profile_picture=self.cleaned_data['profile_picture']
            )

            return professional 

        return user
    
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data