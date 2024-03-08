from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DeleteView, DetailView, UpdateView
from django.contrib import messages

from .models import Professional
from .forms import ProfessionalCreationForm, ProfessionalForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

@method_decorator(user_passes_test(lambda u: u.is_authenticated and (u.is_staff or u.is_superuser)), name='dispatch')
def create_professional(request):
    if request.method == 'POST':
        form = ProfessionalCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profesional creado exitosamente.')
            return redirect(reverse('professional_list'))
        else:
            messages.error(request, 'Error al crear el profesional. Por favor, corrija los errores en el formulario.')
    else:
        form = ProfessionalCreationForm()

    return render(request, 'professional_create.html', {'form': form})


@login_required
def edit_user_view(request, pk):
    template_name = 'professional_detail.html'
    professional = get_object_or_404(Professional, id=pk)

    if not (request.user.is_staff or request.user.is_superuser):
        form = ProfessionalForm(user_is_staff=False, initial={'password': professional.user.password, 'email': professional.user.email, 'telefono': professional.telefono})
    else:
        form = ProfessionalForm(user_is_staff=True, instance=professional)

    if request.method == 'POST':
        form = ProfessionalForm(request.POST, request.FILES, instance=professional, user_is_staff=request.user.is_staff)
        if form.is_valid():
            form.save()
            return redirect('/professionals/?message=Profesional editado&status=Success')

    return render(request, template_name, {'form': form, 'professional': professional})




def professional_list(request):
    professionals = Professional.objects.all()

    name_filter = request.GET.get('name', '')
    if name_filter:
        professionals = professionals.filter(first_name__icontains=name_filter)

    surname_filter = request.GET.get('surname', '')
    if surname_filter:
        professionals = professionals.filter(last_name__icontains=surname_filter)

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

@method_decorator(user_passes_test(lambda u: u.is_authenticated and (u.is_staff or u.is_superuser)), name='dispatch')
def delete_professional(request, id):
    professional = get_object_or_404(Professional, id=id)
    professionals = Professional.objects.all()

    if request.method == 'POST':
        if request.user.is_superuser:
            professional.delete()
            messages.success(request, 'Profesional eliminado exitosamente.')\
            
            return render(request, 'professional_list.html', {'professionals': professionals})
        else:
            return render(request, '403.html')
         

    return render(request, 'professional_list.html', {'professionals': professionals})

