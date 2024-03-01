# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from .models import Professional
from .forms import ProfessionalForm


def professional_detail_view(request, pk):
    professional = get_object_or_404(Professional, pk=pk)

    # Puedes agregar cualquier otra lógica que necesites aquí

    context = {
        'professional': professional,
        'request': request,
    }

    return render(request, 'professional_detail.html', context)

def professional_update_view(request, pk):
    professional = get_object_or_404(Professional, pk=pk)

    if request.method == 'POST':
        form = ProfessionalForm(request.POST, instance=professional)
        if form.is_valid():
            form.save()
            return redirect('professional_detail', pk=pk)  # Ajusta el nombre de la URL según tu configuración
    else:
        form = ProfessionalForm(instance=professional)

    context = {
        'form': form,
        'professional': professional,
        'request': request,
    }

    return render(request, 'professional_form.html', context)


