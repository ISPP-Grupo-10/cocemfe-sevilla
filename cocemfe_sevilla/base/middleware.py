from django.shortcuts import redirect
from django.urls import reverse

class CheckUserStatusMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        user = request.user

        if user.is_authenticated and not user.terms_accepted and request.path != reverse('base:politica_terminos'):
            return redirect(reverse('base:politica_terminos'))

        return response
