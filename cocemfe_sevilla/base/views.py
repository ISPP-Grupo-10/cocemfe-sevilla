from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import AceptarTerminosForm

#@login_required
def pagina_base(request):
    return render(request, 'index.html')

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