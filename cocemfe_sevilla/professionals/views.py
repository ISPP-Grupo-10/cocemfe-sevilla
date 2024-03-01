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
