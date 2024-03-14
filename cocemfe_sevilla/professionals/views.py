from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib import messages

from .models import Professional, Request
from .forms import ProfessionalCreationForm, ProfessionalForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout, login, authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from .forms import ProfessionalForm, RequestCreateForm, RequestUpdateForm

def custom_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            professional = Professional.objects.get(email=email)
            username = professional.username
        except Professional.DoesNotExist:
            error_message = "Nombre de usuario o contraseña incorrectos."
            return render(request, 'registration/login.html', {'error_message': error_message})
        
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

def is_admin(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(is_admin)
def create_professional(request):
    if request.method == 'POST':
        form = ProfessionalCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profesional creado exitosamente.')
            return redirect(reverse('professionals:professional_list'))
        else:
            messages.error(request, 'Error al crear el profesional. Por favor, corrija los errores en el formulario.')
    else:
        form = ProfessionalCreationForm()

    return render(request, 'professional_create.html', {'form': form})


@login_required
def edit_user_view(request, pk):
    template_name = 'professional_detail.html'
    professional = get_object_or_404(Professional, id=pk)
    user_is_staff = request.user.is_staff or request.user.is_superuser
    if request.method == 'GET':
        form = ProfessionalForm(user_is_staff=user_is_staff, instance=professional)
        return render(request, template_name, {'form': form, 'professional': professional})

    #form = ProfessionalForm(instance=professional)
    if request.method == 'POST':
        form = ProfessionalForm(request.POST, request.FILES, user_is_staff=user_is_staff, instance=professional)
        if form.is_valid():
            if user_is_staff:
                form.save()
                return redirect('/professionals/?message=Profesional editado&status=Success')
            elif request.user.id == professional.id:
                form.save()
                return redirect('/professionals/?message=Datos de perfil actualizados&status=Success')
            else:
                return render(request, '403.html')
        else:
            return render(request, template_name, {'form': form, 'professional': professional})



def professional_list(request):
    professionals = Professional.objects.filter(is_superuser=False)

    professionals = professionals.filter(is_staff=False)
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
    professionals = Professional.objects.filter(is_superuser=False)

    if request.method == 'POST':
        if request.user.is_superuser:
            professional.delete()
            messages.success(request, 'Profesional eliminado exitosamente.')\
            
            return render(request, 'professional_list.html', {'professionals': professionals})
        else:
            return render(request, '403.html')
         

    return render(request, 'professional_list.html', {'professionals': professionals})

def create_request(request):
    if request.method == 'POST':
        form = RequestCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/login.html') 
    else:
        form = RequestCreateForm()
    return render(request, 'create_request.html', {'form': form})

@user_passes_test(is_admin)
def update_request(request, pk):
    db_request = get_object_or_404(Request, pk=pk)
    if request.method == 'POST':
        form = RequestUpdateForm(request.POST, instance=db_request)
        if form.is_valid():
            form.save()
            return redirect('professionals:request_list') 
    else:
        form = RequestUpdateForm(instance=db_request)
    return render(request, 'update_request.html', {'form': form, 'email':db_request.email , 'description': db_request.description})

@user_passes_test(is_admin)
def request_list(request):
    requests = Request.objects.all()
    return render(request, 'list_requests.html', {'requests': requests})

