from django.shortcuts import render, redirect, get_object_or_404
from .forms import PDFUploadForm
from .models import Document
from django.utils import timezone

# Create your views here.
def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.start_date = timezone.now().date()
            document.status = False
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
            form.save()
            return redirect('list_pdf')
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
