from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import AceptarTerminosForm
from documents.models import Document

@login_required
def pagina_base(request):
    
    if request.user.is_superuser:
        documentos = Document.objects.all()
    else:
        documentos = Document.objects.filter(professionals=request.user)

    name = request.GET.get('name')

    if name:
        documentos = documentos.filter(name__icontains=name)

    return render(request, 'user_dashboard.html' , {'documentos': documentos})

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

def error_404(request, exception):
    return render(request, '404.html', status=404)

def error_500(request):
    return render(request, '500.html', status=500)
