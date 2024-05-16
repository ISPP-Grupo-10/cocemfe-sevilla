from django.http import HttpResponseRedirect
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
    


class CustomRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404 and not request.path.startswith('/error/404/') and not request.path.startswith('/static/pdfjs/web/viewer.html'):
            print(request.path)
            error_404_url = reverse('error_404')
            return HttpResponseRedirect(error_404_url)
        if response.status_code == 500 and not request.path.startswith('/error/500/') and not request.path.startswith('/static/pdfjs/web/viewer.html'):
            error_500_url = reverse('error_500')
            return HttpResponseRedirect(error_500_url)
        return response
