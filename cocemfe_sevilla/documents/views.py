from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PDFUploadForm
from django.contrib.auth.decorators import login_required
from .models import Document
from suggestions.models import Suggestion
from django.utils import timezone
from django.contrib import messages
from professionals.models import Professional
from chat_messages.models import ChatMessage
from chat_messages.forms import MessageForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.conf import settings
<<<<<<< HEAD
from selenium import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui
import time
import os
=======
import os
from django.http import JsonResponse
from calendars.views import create_event
from datetime import datetime, time
from django.forms.models import model_to_dict
from calendars.views import edit_event_from_document
>>>>>>> develop

@login_required
def upload_pdf(request):
    if request.user.is_superuser:
        professionals = Professional.objects.filter(is_superuser=False)
        if request.method == 'POST':
            form = PDFUploadForm(request.POST, request.FILES)
            if form.is_valid():
                suggestion_end_date = form.cleaned_data['suggestion_end_date']
                suggestion_start_date = form.cleaned_data['suggestion_start_date']
                voting_end_date = form.cleaned_data['voting_end_date']
                document = form.save(commit=False)
                document.voting_start_date = suggestion_end_date
                if suggestion_start_date and suggestion_start_date.date() == timezone.now().date():
                    document.status = 'Aportaciones'
                if suggestion_end_date and suggestion_end_date.date() == timezone.now().date():
                    document.status = 'Votaciones'
                professionals = form.cleaned_data['professionals']
                document.save()
                document.professionals.set(professionals)
                document.save()

                # Obtener el directorio de descarga
                download_directory = os.path.dirname(document.pdf_file.path)
                selenium_converter(document.pdf_file.path, download_directory)

                # Enviar correo electrónico a cada profesional asignado
                subject = 'Nuevo plan de accesibilidad'
                from_email = 'cocemfesevillanotificaciones@gmail.com'
                for professional in professionals:
                    # Renderizar el mensaje de correo electrónico desde un template
                    message = render_to_string('email/new_document_notification.txt', {'document': document, 'professional': professional})
                    send_mail(subject, message, from_email, [professional.email], fail_silently=False)
<<<<<<< HEAD
                return redirect('list_pdf')
=======
                    
                if suggestion_start_date:
                    create_event(request = request, title=f'Inicio: {document.name}', description='Inicio periodo aportaciones', creator= request.user, event_datetime=datetime.combine(suggestion_start_date, time(23, 59, 00)), document=document, type='aportaciones')
                if suggestion_end_date:
                    create_event(request = request, title=f'Final: {document.name}', description='Final periodo aportaciones', creator= request.user, event_datetime=datetime.combine(suggestion_end_date, time(23, 59, 00)), document=document, type='aportaciones')
                    create_event(request = request, title=f'Inicio: {document.name}', description='Inicio periodo votaciones', creator= request.user, event_datetime=datetime.combine(suggestion_end_date, time(23, 59, 00)), document=document, type='votaciones')
                if voting_end_date:
                    create_event(request = request, title=f'Final: {document.name}', description='Final periodo votaciones', creator= request.user, event_datetime=datetime.combine(voting_end_date, time(23, 59, 00)), document=document, type='votaciones')
                return redirect('view_pdf_admin', document.id)
>>>>>>> develop
        else:
            form = PDFUploadForm()
        return render(request, 'upload_pdf.html', {'form': form, 'professionals_not_superuser': professionals})
    else:
        return render(request, '403.html')

def selenium_converter(file_path, download_directory):
    webdriver_path = "/static/selenium/chromedriver.exe"

    # Configuración del navegador
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--ignore-urlfetcher-cert-requests')
    prefs = {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
    }
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.pdf2go.com/es/convertir-de-pdf')  # Reemplaza 'URL_de_la_página_web' con la URL de la página que deseas automatizar

    try:
        driver.maximize_window()

        # Esperar hasta que el botón esté presente en la página
        print("antes del boton")
        #consent_paragraph = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='fc-consent-root']//div[@class='fc-dialog-container']//div[@class='fc-dialog fc-choice-dialog']//div[@class='fc-footer-buttons-container']//div[@class='fc-footer-buttons']//button[@class='fc-button fc-cta-consent fc-primary-button']//p[text()='Consentir']")))
        cookie_panel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fc-consent-root")))
        driver.execute_script("arguments[0].parentNode.removeChild(arguments[0])", cookie_panel)
        #button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Consentir']")))
        # Hacer clic en el botón
        print("despues del boton")
        #consent_paragraph.click()
        print("despues del click")
        # Esperar hasta que la página esté completamente cargada
        button = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,  "//div[@class='upload-container']//button[contains(., 'Seleccionar archivo')]")))
        print("despues del boton 2")
        # Encontrar y hacer clic en el botón
        button = driver.find_element(By.XPATH, "//div[@class='upload-container']//button[contains(., 'Seleccionar archivo')]")
        print("despues del boton 3")
        button.click()
        print("hago click")

        time.sleep(2)
        pyautogui.write(file_path)
        pyautogui.press('enter')
        time.sleep(5)
        # Ejecutar script de JavaScript para desplazarse hacia abajo en la página
        driver.execute_script("window.scrollBy(0, 800);")
        print("despues del scroll")

        form = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "sendform")))
        print("despues del form")
        # Localizar el elemento <strong> con texto "Empezar" dentro del formulario
        empezar_button = form.find_element(By.XPATH, '//form[@id="sendform"]//strong[contains(., "Empezar")]')
        print("despues del boton 4")
        empezar_button.click()

        # Eliminar el archivo original
        #C:\Users\danie\OneDrive\Desktop\ISPP\cocemfe-sevilla-1\cocemfe_sevilla\media\pdfs\PRUEBA-2.pdf
        os.remove(file_path)

        time.sleep(2)


        
        cookie_panel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fc-consent-root")))
        driver.execute_script("arguments[0].parentNode.removeChild(arguments[0])", cookie_panel)
        print("Despues de quitar consent")
        #Pantalla de Consentir


        # Esperar hasta que el enlace de descarga esté presente y hacer clic en él
        #descargar_link = driver.find_element((By.XPATH, '//div[@id="app"]//span[contains(., "Descargar")]'))
        descargar_link = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="app"]//span[contains(., "Descargar")]')))
        print("Boton de descargar visto")
        descargar_link.click()
        print("despues del boton 5")


        # Puedes agregar más acciones aquí, como enviar texto a campos de entrada, hacer clic en enlaces, etc.

        time.sleep(5)

    finally:
        # Cerrar el navegador al finalizar
        driver.quit()        

def view_pdf(request, pk):
    pdf = get_object_or_404(Document, pk=pk)
    professional=request.user
    suggestions = Suggestion.objects.filter(document=pdf)
    paginator = Paginator(suggestions, 5)  # Divide los comentarios en páginas de 10 comentarios cada una
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if professional in pdf.professionals.all():
        return render(request, 'view_pdf.html', {'pdf': pdf, 'page_obj': page_obj})
    else:
        return render(request, '403.html')

@login_required
def view_pdf_admin(request, pk):
    pdf = get_object_or_404(Document, pk=pk)
    suggestions = Suggestion.objects.filter(document=pdf)
    paginator = Paginator(suggestions, 5)  # Divide los comentarios en páginas de 10 comentarios cada una
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    votes_info = {}

    for suggestion in suggestions:
        votes = suggestion.votings.all()  # Recupera todos los votos asociados a la sugerencia
        favor_count = votes.filter(vote=True).count()  # Cuenta los votos a favor
        against_count = votes.filter(vote=False).count()  # Cuenta los votos en contra
        votes_info[suggestion.id] = {'favor_count': favor_count, 'against_count': against_count}
    
        
    context = {
        'pdf': pdf,
        'page_obj': page_obj,
        'votes_info': votes_info,
    }

    if request.user.is_superuser:
        if pdf.status == 'Borrador':
            if pdf.suggestion_start_date and pdf.suggestion_end_date and pdf.professionals.all():
                mensaje = None
            else:
                mensaje = "Debe indicar las fechas de inicio y fin de sugerencia y seleccionar al menos un profesional."

            context = {
                'pdf': pdf,
                'page_obj': page_obj,
                'votes_info': votes_info,
                'mensaje': mensaje,
            }
            return render(request, 'view_pdf.html', context)
        else:
            #El page_obj son los comentarios que se han hecho del doc, si que es verdad que si esta en Borrador no deberia haber nignuno.
            return render(request, 'view_pdf.html', context)
    elif request.user in pdf.professionals.all():
        if pdf.status == 'Borrador':
            if pdf.suggestion_start_date and pdf.suggestion_end_date and pdf.professionals.all():
                mensaje = None
            else:
                mensaje = "Debe indicar las fechas de inicio y fin de sugerencia y seleccionar al menos un profesional."

            context = {
                'pdf': pdf,
                'page_obj': page_obj,
                'votes_info': votes_info,
                'mensaje': mensaje,
            }

            return render(request, 'view_pdf.html', context)
        else:
            #Aquí iría la lógica para otros estados
            #De momento solo esta aportaciones que se deben ver los comentarios del pdf por eso se pode page_obj
            return render(request, 'view_pdf.html', context)
    else:
        return render(request, '403.html')
    
@login_required
def update_pdf(request, pk):
    document = get_object_or_404(Document, pk=pk)
    old_suggestion_start_date = document.suggestion_start_date.astimezone(timezone.get_current_timezone()) if document.suggestion_start_date else None
    old_suggestion_end_date = document.suggestion_end_date.astimezone(timezone.get_current_timezone()) if document.suggestion_end_date else None
    old_voting_end_date = document.voting_end_date.astimezone(timezone.get_current_timezone()) if document.voting_end_date else None
    professionals_not_superuser = Professional.objects.filter(is_superuser=False)
    if request.user.is_superuser:
        if request.method == 'POST':
            form = PDFUploadForm(request.POST, request.FILES, instance=document)
            if form.is_valid():
                suggestion_start_date = form.cleaned_data['suggestion_start_date']
                suggestion_end_date = form.cleaned_data['suggestion_end_date']
                voting_end_date = form.cleaned_data['voting_end_date']
                pdf = form.cleaned_data['pdf_file']

                updated_document = form.save(commit=False)
                updated_document.pdf_file = pdf

                previous_status = document.status      

                if suggestion_start_date and suggestion_start_date.date() == timezone.now().date():
                    updated_document.status = 'Aportaciones'
                if suggestion_end_date and suggestion_end_date.date() == timezone.now().date():
                    updated_document.status = 'Votaciones'

                updated_document.voting_start_date = suggestion_end_date

                updated_document.save()

                if updated_document.status != previous_status:
                    subject = f'Cambio de estado del documento: {updated_document.name}'
                    from_email = settings.EMAIL_HOST_USER
                    for professional in updated_document.professionals.all():
                        message = render_to_string('email/status_updated.txt', {
                            'document': updated_document,
                            'professional': professional,
                            'previous_status': previous_status
                        })
                        send_mail(subject, message, from_email, [professional.email], fail_silently=False)

                form.save_m2m()

                if suggestion_start_date and suggestion_start_date != old_suggestion_start_date:
                    if old_suggestion_start_date is None:
                        create_event(request = request, title=f'Inicio: {document.name}', description='Inicio periodo aportaciones', creator= request.user, event_datetime=datetime.combine(suggestion_start_date, time(23, 59, 00)), document=document, type='aportaciones')
                    else:
                        edit_event_from_document(request=request, document_id=pk, type='aportaciones', old_datetime=datetime.combine(old_suggestion_start_date, time(23, 59, 00)), new_datetime=datetime.combine(suggestion_start_date, time(23, 59, 00)))
                if suggestion_end_date and suggestion_end_date != old_suggestion_end_date:
                    if old_suggestion_end_date is None:
                        create_event(request = request, title=f'Final: {document.name}', description='Final periodo aportaciones', creator= request.user, event_datetime=datetime.combine(suggestion_end_date, time(23, 59, 00)), document=document, type='aportaciones')
                        create_event(request = request, title=f'Inicio: {document.name}', description='Inicio periodo votaciones', creator= request.user, event_datetime=datetime.combine(suggestion_end_date, time(23, 59, 00)), document=document, type='votaciones')
                    else:
                        edit_event_from_document(request=request, document_id=pk, type='aportaciones', old_datetime=datetime.combine(old_suggestion_end_date, time(23, 59, 00)), new_datetime=datetime.combine(suggestion_end_date, time(23, 59, 00)))
                        edit_event_from_document(request=request, document_id=pk, type='votaciones', old_datetime=datetime.combine(old_suggestion_end_date, time(23, 59, 00)), new_datetime=datetime.combine(suggestion_end_date, time(23, 59, 00)))
                if voting_end_date and voting_end_date != old_voting_end_date:
                    if old_voting_end_date is None:
                        create_event(request = request, title=f'Final: {document.name}', description='Final periodo votaciones', creator= request.user, event_datetime=datetime.combine(voting_end_date, time(23, 59, 00)), document=document, type='votaciones')
                    else:
                        edit_event_from_document(request=request, document_id=pk, type='votaciones', old_datetime=datetime.combine(old_voting_end_date, time(23, 59, 00)), new_datetime=datetime.combine(voting_end_date, time(23, 59, 00)))
                
                
                return redirect('view_pdf_admin', updated_document.id)
        else:
            form = PDFUploadForm(instance=document)
        return render(request, 'update_pdf.html', {'form': form, 'document': document, 'professionals_not_superuser': professionals_not_superuser})
    else:
        return render(request, '403.html')



@login_required
def delete_pdf_form(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.user.is_superuser:
        file_path = document.pdf_file.path

        if os.path.exists(file_path):
            os.remove(file_path)

        document.pdf_file = None
        document.save()

        return JsonResponse({'message': 'Archivo adjunto eliminado correctamente'})
    else:
        return JsonResponse({'error': 'No tienes permiso para eliminar este archivo adjunto'}, status=403)

@login_required
def delete_pdf(request, pk):
    
    document = get_object_or_404(Document, pk=pk)
    if request.user.is_superuser:
        document.delete()
        return redirect('list_pdf')
    else:
        return render(request, '403.html')

@login_required
def list_pdf(request):
    if request.user.is_superuser:
        documentos = Document.objects.all()
    else:
        documentos = Document.objects.filter(professionals=request.user)

    name = request.GET.get('name')
    status = request.GET.get('status')
    suggestion_start_date = request.GET.get('suggestion_start_date')

    if name:
        documentos = documentos.filter(name__icontains=name)
    if status:
        documentos = documentos.filter(status=status)
    if suggestion_start_date:
        try:
            # Intenta convertir la entrada del filtro de fecha en un objeto de fecha
            suggestion_start_date = timezone.datetime.strptime(suggestion_start_date, '%Y-%m-%d').date()
        except ValueError:
            # Si la entrada no es una fecha válida, muestra un mensaje de error
            messages.error(request, "La fecha de inicio no es válida. Utilice el formato AAAA-MM-DD.")
            return render(request, "list_pdf.html", {'documentos': documentos, 'Document': Document})

        # Ahora puedes usar suggestion_start_date en tus filtros
        documentos = documentos.filter(suggestion_start_date=suggestion_start_date)

    return render(request, "list_pdf.html", {'documentos': documentos, 'Document': Document})

@login_required
def load_comments(request, pk):
    doc = get_object_or_404(Document, id=pk)
    if request.user in doc.professionals.all() or request.user.is_staff:
        comments = ChatMessage.objects.filter(document=doc)
        return render(request, 'list_comments.html', {'doc': doc, 'chat_messages': comments})
    else:
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

@login_required
def publish_comment(request, pk):
    doc = get_object_or_404(Document, id=pk)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.document = doc
            comment.post_date = timezone.now()
            comment.save()
            return redirect('view_pdf_chat', pk=doc.id)
    else:
        form = MessageForm()
    comments = ChatMessage.objects.filter(document=doc)
    return render(request, 'list_comments.html', {'doc': doc, 'chat_messages': comments, 'form': form})

@login_required
def check_pdf(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    if request.user not in doc.checked_professionals.all():
        doc.checked_professionals.add(request.user)
    doc.save()
    return redirect('view_pdf_admin', pk=pk)