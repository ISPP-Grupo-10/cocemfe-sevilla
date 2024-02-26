from django.shortcuts import render, redirect, get_object_or_404
from .forms import PDFUploadForm
from .models import Document
from django.utils import timezone
from django.contrib import messages
# Create your views here.

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            document = form.save(commit=False)
            document.start_date = timezone.now().date()
            document.status = False
            professionals = form.cleaned_data['professionals']
            document.save()
            document.professionals.set(professionals)
            document.save()
            return redirect('list_pdf')
    else:
        form = PDFUploadForm()
    return render(request, 'upload_pdf.html', {'form': form})

def view_pdf(request, pk):
    pdf = get_object_or_404(Document, pk=pk)
    return render(request, 'view_pdf.html', {'pdf': pdf})

def update_pdf(request,pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, instance=document)
        if form.is_valid():
            end_date = form.cleaned_data['end_date']
            professionals = form.cleaned_data['professionals']
            if end_date > timezone.now().date():
                form.save()
                document.professionals.set(professionals)
                return redirect('list_pdf')
            else:
                messages.error(request, "La fecha de finalización debe ser posterior a la fecha actual.")
        else:
            messages.error(request, "Por favor completa todos los campos del formulario.")
    else:
        form = PDFUploadForm(instance=document)
    return render(request, 'update_pdf.html', {'form': form, 'document': document})

def delete_pdf(request, pk):
    document = get_object_or_404(Document, pk=pk)
    document.delete()
    return redirect('list_pdf')  

def list_pdf(request):
    documentos = Document.objects.all()
    return render(request, "list_pdf.html", {'documentos': documentos})

