from django.shortcuts import render, redirect, get_object_or_404
from .forms import PDFUploadForm
from .models import Document
from django.utils import timezone
from django.contrib import messages
# Create your views here.
def upload_pdf(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = PDFUploadForm(request.POST, request.FILES)
            if form.is_valid():
                end_date = form.cleaned_data['end_date']
                pdf_file = form.cleaned_data['pdf_file']
                if end_date > timezone.now().date():
                    if pdf_file.name.endswith('.pdf'):
                        document = form.save(commit=False)
                        document.start_date = timezone.now().date()
                        document.status = False
                        document.save()
                        return redirect('upload_pdf')
                    else:
                        messages.error(request, "El archivo debe ser un PDF.")
                else:
                    messages.error(request, "La fecha de finalización debe ser posterior a la fecha actual.")
        else:
            form = PDFUploadForm()
        return render(request, 'upload_pdf.html', {'form': form})
    else:
        return render(request, '403.html')

def view_pdf(request, pk):
    pdf = get_object_or_404(Document, pk=pk)
    return render(request, 'view_pdf.html', {'pdf': pdf})

def docsList(request):

    documentos = Document.objects.all()
    return render(request, "docsList.html", {'documentos': documentos})