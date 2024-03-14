from django import forms

class AceptarTerminosForm(forms.Form):
    aceptar_terminos = forms.BooleanField(label='Acepto los términos y condiciones')
