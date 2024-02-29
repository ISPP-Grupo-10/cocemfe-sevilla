# views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from .models import Professional
from .forms import ProfessionalForm

class ProfessionalDetailView(DetailView):
    model = Professional
    template_name = 'professional_detail.html'
    context_object_name = 'professional'

class ProfessionalUpdateView(UpdateView):
    model = Professional
    form_class = ProfessionalForm
    template_name = 'professional_form.html'
    success_url = reverse_lazy('professional_detail')  # Ajusta el nombre de la URL según tu configuración


