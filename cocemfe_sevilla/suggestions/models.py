from django.db import models
from documents.models import Document
from professionals.models import Professional
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.validators import MinLengthValidator, MinValueValidator

class Suggestion(models.Model):
    RELEVANCE_CHOICES = (
        ('Muy importante', 'Muy importante'),
        ('Importante', 'Importante'),
        ('Poco importante', 'Poco importante'),
    )
    main = models.CharField(max_length=255, validators=[MinLengthValidator(1)])
    justification = models.TextField(max_length=500, validators=[MinLengthValidator(1)])
    relevance = models.CharField(max_length=20, choices=RELEVANCE_CHOICES)
    section = models.CharField(max_length=2000, validators=[MinLengthValidator(1)])
    page = models.IntegerField(validators=[MinValueValidator(0)])
    date = models.DateField()

    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, null=True, related_name='suggestions')
    document = models.ForeignKey(Document, on_delete=models.CASCADE, null=True, related_name='suggestions')

    def __str__(self):
        return self.main

    def clean(self):
        super().clean()

        # Validación: Verificar que la fecha de la sugerencia no sea en el futuro.
        if self.date > timezone.now().date():
            raise ValidationError("La fecha de la sugerencia no puede ser en el futuro.")

        # Validación: Verificar que los objetos relacionados existan en la base de datos.
        if self.professional_id is not None and not Professional.objects.filter(pk=self.professional_id).exists():
            raise ValidationError("El profesional especificado no existe.")
        if self.document_id is not None and not Document.objects.filter(pk=self.document_id).exists():
            raise ValidationError("El documento especificado no existe.")

        # Validación: Verificar que la opción de relevancia seleccionada sea una de las opciones válidas.
        valid_relevance_choices = [choice[0] for choice in self.RELEVANCE_CHOICES]
        if self.relevance not in valid_relevance_choices:
            raise ValidationError("La relevancia seleccionada no es válida.")

        # Validación: Requerir que se proporcione una justificación para cada sugerencia.
        if not self.justification:
            raise ValidationError("Se requiere una justificación para la sugerencia.")

        # Validación: Requerir que se proporcione una sección para cada sugerencia.
        if not self.section:
            raise ValidationError("Se requiere una sección para la sugerencia.")
        
        # Validación: Verificar que la longitud de la sección no exceda cierto valor.
        if len(self.section) > 2000:
            raise ValidationError("La sección de la sugerencia no puede exceder los 2000 caracteres.")
        
        # Validación: Verificar que la longitud del campo 'main' no exceda cierto valor.
        if len(self.main) > 255:
            raise ValidationError("El campo 'main' no puede exceder los 255 caracteres.")
        
        # Validación: Verificar que el campo 'page' sea un número entero positivo.
        if self.page < 0:
            raise ValidationError("El número de página debe ser un entero positivo.")
        
        # Validación: Verificar que la longitud de la justificación no exceda cierto valor.
        if len(self.justification) > 500:
            raise ValidationError("La justificación de la sugerencia no puede exceder los 500 caracteres.")
