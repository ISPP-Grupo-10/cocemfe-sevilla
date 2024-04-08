import re
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils.http import urlsafe_base64_decode
import requests
import json
from django.utils.encoding import force_str

import requests

from .models import Professional

def validate_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.compile(patron).match(email)

def get_professional(uidb64):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(Professional, pk=uid)
    except (TypeError, ValueError, OverflowError, Professional.DoesNotExist):
        user = None
    return user