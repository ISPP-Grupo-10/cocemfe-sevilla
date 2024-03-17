import random
import string
from django import forms
from django.contrib.auth import get_user_model
from organizations.models import Organization
from .models import Professional, Request
from django import forms
from .models import Professional


class ProfessionalForm(forms.ModelForm):
    class Meta:
        model = Professional
        fields = ['username', 'first_name', 'last_name', 'password', 'telephone_number', 'license_number', 'organizations', 'email', 'profile_picture']
        widgets = {
            'password': forms.PasswordInput(), 
        }

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
            
        self.fields.pop('password')

    def clean_email(self):
        if not (self.instance.is_superuser or self.instance.is_staff):
            return self.cleaned_data.get('email', self.instance.email)
        return self.cleaned_data['email']

    def clean_password(self):
        if not (self.instance.is_superuser or self.instance.is_staff):
            password = self.cleaned_data.get('password')
            if password:
                return password
            return self.instance.password
        return self.cleaned_data['password']

    def clean_telephone_number(self):
        if not (self.instance.is_superuser or self.instance.is_staff):
            return self.cleaned_data.get('telephone_number', self.instance.telephone_number)
        return self.cleaned_data['telephone_number']

    def clean_username(self):
        if not (self.instance.is_superuser or self.instance.is_staff):
            return self.cleaned_data.get('username', self.instance.username)
        return self.cleaned_data['username']

    def clean_first_name(self):
        if not (self.instance.is_superuser or self.instance.is_staff):
            return self.cleaned_data.get('first_name', self.instance.first_name)
        return self.cleaned_data['first_name']

    def clean_last_name(self):
        if not (self.instance.is_superuser or self.instance.is_staff):
            return self.cleaned_data.get('last_name', self.instance.last_name)
        return self.cleaned_data['last_name']

    def clean_license_number(self):
        if not (self.instance.is_superuser or self.instance.is_staff):
            return self.cleaned_data.get('license_number', self.instance.license_number)
        return self.cleaned_data['license_number']

    def clean_organizations(self):
        if not (self.instance.is_superuser or self.instance.is_staff):
            return self.cleaned_data.get('organizations', self.instance.organizations)
        return self.cleaned_data['organizations']

    def clean_profile_picture(self):
        if not (self.instance.is_superuser or self.instance.is_staff):
            return self.cleaned_data.get('profile_picture', self.instance.profile_picture)
        return self.cleaned_data['profile_picture']
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            instance.set_password(password)
        if commit:
            instance.save()
        return instance


class ProfessionalCreationForm(forms.ModelForm):
    class Meta:
        model = Professional
        fields = ['username', 'first_name', 'last_name', 'email', 'telephone_number', 'license_number', 'organizations', 'profile_picture']

    telephone_number = forms.CharField(max_length=9, validators=[Professional.phone_number_validator])
    license_number = forms.CharField(max_length=20)
    organizations = forms.ModelChoiceField(queryset=Organization.objects.all())
    profile_picture = forms.ImageField(required=False)

    def save(self, commit=True):
        professional = super().save(commit=False)

        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        professional.set_password(password)

        if commit:
            professional.save()

        return professional

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
