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
import os
from django.http import JsonResponse

@login_required
def upload_pdf(request):
    if request.user.is_superuser:
        professionals = Professional.objects.filter(is_superuser=False)
        if request.method == 'POST':
            form = PDFUploadForm(request.POST, request.FILES)
            if form.is_valid():
                suggestion_end_date = form.cleaned_data['suggestion_end_date']
                suggestion_start_date = form.cleaned_data['suggestion_start_date']
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
                # Enviar correo electrónico a cada profesional asignado
                subject = 'Nuevo plan de accesibilidad'
                from_email = settings.EMAIL_HOST_USER
                for professional in professionals:
                    # Renderizar el mensaje de correo electrónico desde un template
                    message = render_to_string('email/new_document_notification.txt', {'document': document, 'professional': professional})
                    send_mail(subject, message, from_email, [professional.email], fail_silently=False)
                return redirect('view_pdf_admin', document.id)
        else:
            form = PDFUploadForm()
        return render(request, 'upload_pdf.html', {'form': form, 'professionals_not_superuser': professionals})
    else:
        return render(request, '403.html')

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
    professionals_not_superuser = Professional.objects.filter(is_superuser=False)
    if request.user.is_superuser:
        if request.method == 'POST':
            form = PDFUploadForm(request.POST, request.FILES, instance=document)
            if form.is_valid():
                suggestion_start_date = form.cleaned_data['suggestion_start_date']
                suggestion_end_date = form.cleaned_data['suggestion_end_date']
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