from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PDFUploadForm
from .models import Document
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from professionals.models import Professional
from chat_messages.models import ChatMessage
from chat_messages.forms import MessageForm


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
                return redirect('list_pdf')
               
        else:
            form = PDFUploadForm()
        return render(request, 'upload_pdf.html', {'form': form, 'professionals_not_superuser': professionals})
    else:
        return render(request, '403.html')


def view_pdf(request, pk):
    pdf = get_object_or_404(Document, pk=pk)
    professional=request.user
    if professional in pdf.professionals.all():
        return render(request, 'view_pdf.html', {'pdf': pdf})
    else:
        return render(request, '403.html')

def view_pdf_admin(request, pk):
    pdf = get_object_or_404(Document, pk=pk)
    if request.user.is_superuser:
        if pdf.status == 'Borrador':
            if pdf.suggestion_start_date and pdf.suggestion_end_date and pdf.professionals.all():
                mensaje = None
            else:
                mensaje = "Debe indicar las fechas de inicio y fin de sugerencia y seleccionar al menos un profesional."
                
            return render(request, 'view_pdf.html', {'pdf': pdf, 'mensaje': mensaje})
        else:
            return render(request, 'view_pdf.html', {'pdf': pdf})
    elif request.user in pdf.professionals.all():
        if pdf.status == 'Borrador':
            if pdf.suggestion_start_date and pdf.suggestion_end_date and pdf.professionals.all():
                mensaje = None
            else:
                mensaje = "Debe indicar las fechas de inicio y fin de sugerencia y seleccionar al menos un profesional."
            return render(request, 'view_pdf.html', {'pdf': pdf, 'mensaje': mensaje})
        else:
            #Aquí iría la lógica para otros estados
            return render(request, 'view_pdf.html', {'pdf': pdf})
    else:
        return render(request, '403.html')
    

from django.shortcuts import redirect

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
                
                if suggestion_start_date and suggestion_start_date.date() == timezone.now().date():
                    updated_document.status = 'Aportaciones'
                if suggestion_end_date and suggestion_end_date.date() == timezone.now().date():
                    updated_document.status = 'Votaciones'
                
                updated_document.voting_start_date = suggestion_end_date

                updated_document.save()
                form.save_m2m() 
                
                return redirect('list_pdf')
        else:
            form = PDFUploadForm(instance=document)
        return render(request, 'update_pdf.html', {'form': form, 'document': document, 'professionals_not_superuser': professionals_not_superuser})
    else:
        return render(request, '403.html')


def delete_pdf(request, pk):
    
    document = get_object_or_404(Document, pk=pk)
    if request.user.is_superuser:
        document.delete()
        return redirect('list_pdf')   
    else:
        return render(request, '403.html')

def list_pdf(request):
    documentos = Document.objects.all()

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

