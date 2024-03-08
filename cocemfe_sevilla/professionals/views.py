from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DeleteView, DetailView, UpdateView
from django.contrib import messages

from .models import Professional
from .forms import ProfessionalCreationForm, ProfessionalForm
from django.contrib.auth.decorators import login_required, staff_member_required

#solo adiministradores deben poder acceder a create_professional
@staff_member_required
def create_professional(request):
    print("Entering create_professional view")
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

    print("Rendering create_professional.html with form")
    return render(request, 'professional_create.html', {'form': form})

@staff_member_required
class EditUserView(View):
    def get(self, request, pk):
        professional = get_object_or_404(Professional, id=pk)
        form = ProfessionalForm(instance=professional)
        return render(request, 'professional_detail.html', {'form': form, 'professional': professional})

    def post(self, request, pk):
        professional = get_object_or_404(Professional, id=pk)
        print(request.FILES)
        form = ProfessionalForm(request.POST,request.FILES, instance=professional)
        if form.is_valid():
            if request.user.is_superuser:
                form.save()
                return redirect('/professionals/?message=Profesional editado&status=Success')
            else:
                return render(request, '403.html')
        else:
            return render(request, 'professional_detail.html', {'form': form, 'professional': professional})


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

@staff_member_required
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

