import random
import string
from django import forms
from organizations.models import Organization
from .models import Professional, Request
from django.contrib.auth.hashers import make_password 
from django.forms import ValidationError

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
            self.fields['username'].widget.attrs['readonly'] = True
            self.fields['first_name'].widget.attrs['readonly'] = True
            self.fields['last_name'].widget.attrs['readonly'] = True
            self.fields['license_number'].widget.attrs['readonly'] = True
            # El campo organizations se mantendrá editable pero solo de lectura
            self.fields['organizations']
            self.fields['profile_picture'].widget.attrs['disabled'] = True
            self.fields['profile_picture'].widget.attrs['style'] = 'pointer-events: none;'

            
        self.fields.pop('password')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not (self.instance.is_superuser or self.instance.is_staff):
            if email and Professional.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
                raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return email

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
    password = forms.CharField(widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['readonly'] = False  # Allow editing email field

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Professional.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return email

    def save(self, commit=True):
        professional = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if not password:
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

        hashed_password = make_password(password)
        professional.password = hashed_password

        professional.save()

        return professional, password

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


class SecurePasswordChangeForm(forms.Form):

    @staticmethod
    def validate_password_strength(password):
        if len(password) < 12:
            raise ValidationError(
                ("La contraseña debe tener al menos 12 caracteres."),
                code='password_too_short'
            )
        if not any(char.isupper() for char in password):
            raise ValidationError(
                ("La contraseña debe contener al menos una letra mayúscula."),
                code='password_no_uppercase'
            )
        if not any(char.islower() for char in password):
            raise ValidationError(
                ("La contraseña debe contener al menos una letra minúscula."),
                code='password_no_lowercase'
            )
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                ("La contraseña debe contener al menos un dígito."),
                code='password_no_digit'
            )

        if not any(char in "!@#$%^&*()-_=+[]{};:'\"<>,.?/" for char in password):
            raise ValidationError(
                ("La contraseña debe contener al menos un carácter especial."),
                code='password_no_special_char'
            )


    def __init__(self, data=None, user=None, *args, **kwargs):
        self.user = user
        super().__init__(data, *args, **kwargs)
        self.fields['old_password'] = forms.CharField(
            label='Contraseña antigua',
            widget=forms.PasswordInput(attrs={'class': 'form-control', 'value': ''}))

    old_password = forms.CharField(
        label='Contraseña antigua',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password1 = forms.CharField(
        label='Nueva contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[validate_password_strength]
    )
    new_password2 = forms.CharField(
        label='Confirmar nueva contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if self.user is None:
            raise forms.ValidationError('El usuario no está autenticado.')
        elif not self.user.check_password(old_password):
            raise forms.ValidationError('La contraseña antigua es incorrecta.')
        return old_password

    def clean(self):
        cleaned_data = super().clean()
        if 'new_password1' not in cleaned_data:
            cleaned_data['new_password1'] = ''
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')
        if new_password1 != new_password2 or new_password1 == '':
            raise forms.ValidationError('Las contraseñas nuevas no coinciden.')
        return cleaned_data

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        try:
            self.validate_password_strength(password)
        except forms.ValidationError as e:
            self.add_error('new_password1', e)
            raise
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
