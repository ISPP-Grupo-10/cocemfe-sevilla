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
        
        # Verificar si es un error 404 y no está en la lista de rutas excluidas
        if response.status_code == 404 and not self._is_excluded_path(request.path):
            error_404_url = reverse('error_404')
            return HttpResponseRedirect(error_404_url)
        
        # Verificar si es un error 500 y no está en la lista de rutas excluidas
        if response.status_code == 500 and not self._is_excluded_path(request.path):
            error_500_url = reverse('error_500')
            return HttpResponseRedirect(error_500_url)
        
        return response

    def _is_excluded_path(self, path):
        # Lista de rutas excluidas
        excluded_paths = ['/error/404/', '/error/500/', '/static/', '/media/']
        
        # Verificar si la ruta comienza con alguna de las rutas excluidas
        for excluded_path in excluded_paths:
            if path.startswith(excluded_path):
                return True
        return False
