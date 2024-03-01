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
    success_url = reverse_lazy('professional_detail')


def professional_list(request):
    professionals = Professional.objects.all()

    name_filter = request.GET.get('name', '')
    if name_filter:
        professionals = professionals.filter(name__icontains=name_filter)

    surname_filter = request.GET.get('surname', '')
    if surname_filter:
        professionals = professionals.filter(surname__icontains=surname_filter)

    license_number_filter = request.GET.get('license_number', '')
    if license_number_filter:
        professionals = professionals.filter(license_number__icontains=license_number_filter)

    organization_filter = request.GET.get('organization', '')
    if organization_filter:
        professionals = professionals.filter(organizations__name__icontains=organization_filter)

    return render(request, 'professional_list.html', {
        'professionals': professionals,
        'name_filter': name_filter,
        'surname_filter': surname_filter,
        'license_number_filter': license_number_filter,
        'organization_filter': organization_filter,
    })
