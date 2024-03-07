from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from .models import Professional
from django.contrib.auth.decorators import login_required
from .forms import ProfessionalForm

def custom_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = get_object_or_404(Professional, email = email).username
        print(username)
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = "Nombre de usuario o contraseña incorrectos."
            return render(request, 'registration/login.html', {'error_message': error_message})
    else:
        return render(request, 'registration/login.html')

def custom_logout(request):
    logout(request)
    return redirect('/')

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

@login_required
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

@login_required
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

