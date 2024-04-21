from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from .utils import get_professional
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from documents.models import Document
from .models import Professional, Request
from .forms import ProfessionalCreationForm, ProfessionalForm, SecurePasswordChangeForm, RequestCreateForm, RequestUpdateForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.hashers import make_password 
from django.http import HttpResponseForbidden
import random
import string


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
        if user is not None and (professional.email_verified or professional.is_superuser):
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
            professional = form.save(commit=False)
            professional.save()
  

            password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
            professional.password = make_password(password)
            uid = urlsafe_base64_encode(force_bytes(professional.pk))
            verify_url = reverse('professionals:verify_email', args=[uid])

            subject = '¡Bienvenida a COCEMFE Sevilla - Acceso al Sistema de Gestión de Documentos!'
            
            # Enviar el correo electrónico de verificación
            template = get_template('email/verification_email.html')
            content = template.render(
                {'verify_url': request.build_absolute_uri('/') + verify_url[1:],'professional': professional, 'password': password})
            message = EmailMultiAlternatives(
                subject,
                content,
                settings.EMAIL_HOST_USER,
                [professional.email]
            )
            message.attach_alternative(content, 'text/html')
            message.send()
            return redirect(reverse('professionals:professional_list'))
    else:
        form = ProfessionalCreationForm()

    return render(request, 'professional_create.html', {'form': form})

@login_required
def professional_data(request, professional_id):
    professional = get_object_or_404(Professional, pk=professional_id)
    user_is_staff = request.user.is_staff or request.user.is_superuser
    if user_is_staff or request.user.pk == professional_id:
        professional.password = ''
        return render(request, 'professional_data.html', {'professional': professional})
    else:
        return HttpResponseForbidden("You are not authorized to view this page.")
    
@login_required
def professional_details(request, pk):
    professional = get_object_or_404(Professional, id=pk)
    return render(request, 'professional_details.html', {'professional': professional})

@login_required
def edit_user_view(request, pk):
    template_name = 'professional_detail.html'
    professional = get_object_or_404(Professional, id=pk)
    user_is_staff = request.user.is_staff or request.user.is_superuser
    if request.method == 'GET':
        form = ProfessionalForm(user_is_staff=user_is_staff, instance=professional)
        return render(request, template_name, {'form': form, 'professional': professional})

    if request.method == 'POST':
        form = ProfessionalForm(request.POST, request.FILES, user_is_staff=user_is_staff, instance=professional)
        if form.is_valid():
            if user_is_staff and not request.user.id == professional.id:
                form.save()
                return redirect('/professionals/?message=Profesional editado&status=Success')
            elif request.user.id == professional.id:
                form.save()
                previous_url = request.META.get('HTTP_REFERER')
                if previous_url:
                    return redirect(previous_url + '?message=Datos de perfil actualizados&status=Success')
                else:
                    return redirect('/?message=Datos de perfil actualizados&status=Success')
            else:
                return render(request, '403.html')
        else:
            return render(request, template_name, {'form': form, 'professional': professional})


@user_passes_test(lambda u: u.is_authenticated)
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

@user_passes_test(lambda u: u.is_authenticated and (u.is_staff or u.is_superuser))
def delete_professional(request, id):
    if request.method == 'POST':
        professional = get_object_or_404(Professional, id=id)
        professionals = Professional.objects.filter(is_superuser=False)

        if request.user.is_superuser:
            professional.delete()
            return render(request, 'professional_list.html', {'professionals': professionals})
        else:
            return render(request, '403.html')

    professionals = Professional.objects.filter(is_superuser=False)
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


def request_document_chats(request):
    if request.method == 'GET':
        professional = request.user
        query = request.GET.get('q')  # Obtener el valor de búsqueda del parámetro 'q'
        possessed_documents = []

        if query:  # Si se proporciona un término de búsqueda
            # Filtrar documentos por nombre que contenga el término de búsqueda
            if request.user.is_superuser:
                possessed_documents = Document.objects.filter(name__icontains=query)
            else:
                all_documents = Document.objects.filter(professionals=professional)
                possessed_documents = all_documents.filter(name__icontains=query)
        else:  # Si no hay término de búsqueda, mostrar todos los documentos del usuario
            if request.user.is_superuser:
                possessed_documents = Document.objects.all()
            else:
                possessed_documents = Document.objects.filter(professionals=professional)

        return render(request, 'list_chats.html', {'possessed_documents': possessed_documents})
   

@login_required
def change_password(request):
    if request.method == 'POST':
        form = SecurePasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu contraseña ha sido cambiada exitosamente.')
            return redirect('professionals:request_list') # URL TEMPORAL, INTEGRAR CON PANTALLA PERFIL USUARIO
    else:
        form = SecurePasswordChangeForm(user=request.user)
    return render(request, 'update_password.html', {'form': form})

class VerifyEmailView(View):

    def get(self, request, uidb64):
        professional = get_professional(uidb64)
        if professional is not None:
            professional.email_verified = True
            professional.save()
            return redirect('/?message=Correo_electronico_verificado&status=Success')
        else:
            return redirect('/?message=Correo_electronico_no_verificado&status=Error')
