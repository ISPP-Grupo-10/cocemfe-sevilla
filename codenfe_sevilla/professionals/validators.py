from django.forms import ValidationError

def validate_password_strength(password):
    # Verifica la longitud mínima
    if len(password) < 12:
        raise ValidationError(
            _("La contraseña debe tener al menos 12 caracteres."),
            code='password_too_short'
        )

    # Verifica que haya al menos una mayúscula, una minúscula y un carácter especial
    if not any(char.isupper() for char in password):
        raise ValidationError(
            _("La contraseña debe contener al menos una letra mayúscula."),
            code='password_no_upper'
        )
    if not any(char.islower() for char in password):
        raise ValidationError(
            _("La contraseña debe contener al menos una letra minúscula."),
            code='password_no_lower'
        )
    if not any(char in "!@#$%^&*()-_=+[]{};:'\"<>,.?/" for char in password):
        raise ValidationError(
            _("La contraseña debe contener al menos un carácter especial."),
            code='password_no_special_char'
        )