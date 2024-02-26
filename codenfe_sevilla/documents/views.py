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
            return redirect('upload_pdf')
    else:
        form = PDFUploadForm()
    return render(request, 'upload_pdf.html', {'form': form})

def view_pdf(request, pk):
    pdf = get_object_or_404(Document, pk=pk)
    return render(request, 'view_pdf.html', {'pdf': pdf})

def docsList(request):
    documentos = Document.objects.all()

    name = request.GET.get('name')
    status = request.GET.get('status')
    start_date = request.GET.get('start_date')

    if name:
        documentos = documentos.filter(name__icontains=name)
    if status:
        documentos = documentos.filter(status=status)
    if start_date:
        documentos = documentos.filter(start_date=start_date)

    return render(request, "docsList.html", {'documentos': documentos})