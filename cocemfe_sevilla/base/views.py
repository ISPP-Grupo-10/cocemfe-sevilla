from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import AceptarTerminosForm
from .models import NotificationType
from django.core.mail import send_mail
from django.conf import settings

@login_required
def pagina_base(request):
    return render(request, 'index.html')

def send_email(notification_type, recipients, document=None, previous_status=None, new_status=None):
    if not isinstance(notification_type, NotificationType):
        raise ValueError("Invalid notification type")

    subject = ""
    message = ""

    if notification_type == NotificationType.REVIEWER:
        subject = "Subject for Reviewer"
        message = "Has sido seleccionado como revisor del documento " + document
    elif notification_type == NotificationType.STATUS:
        subject = "Subject for New Document"
        message = "Message for New Document"
    elif notification_type == NotificationType.NEW_SUGGESTION:
        subject = "Subject for New Suggestion"
        message = "Message for New Suggestion"
    elif notification_type == NotificationType.WELCOME:
        subject = "Subject for Welcome"
        message = "Message for Welcome"
    
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        recipients,
        fail_silently=False,
    )

def politica_terminos(request):
    if request.method == 'POST':
        form = AceptarTerminosForm(request.POST)
        if form.is_valid():
            user = request.user
            user.terms_accepted = True
            user.save()
            return HttpResponseRedirect('/')
    else:
        form = AceptarTerminosForm()
    
    return render(request, 'politica_terminos.html', {'form': form})
