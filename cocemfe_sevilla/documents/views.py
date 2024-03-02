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
                        document.status = 'Abierto'
                        professionals = form.cleaned_data['professionals']
                        document.save()
                        document.professionals.set(professionals)
                        document.save()
                        return redirect('list_pdf')
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
    professional=request.user
    if professional in pdf.professionals.all():
        return render(request, 'view_pdf.html', {'pdf': pdf})
    else:
        return render(request, '403.html')

def view_pdf_admin(request, pk):
    pdf = get_object_or_404(Document, pk=pk)
    # falta comprobar si el usuario es admin:
    return render(request, 'view_pdf.html', {'pdf': pdf})
    '''
    else:
        return render(request, '403.html')
    '''

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

    name = request.GET.get('name')
    status = request.GET.get('status')
    start_date = request.GET.get('start_date')

    if name:
        documentos = documentos.filter(name__icontains=name)
    if status:
        documentos = documentos.filter(status=status)
    if start_date:
        try:
            # Intenta convertir la entrada del filtro de fecha en un objeto de fecha
            start_date = timezone.datetime.strptime(start_date, '%Y-%m-%d').date()
        except ValueError:
            # Si la entrada no es una fecha válida, muestra un mensaje de error
            messages.error(request, "La fecha de inicio no es válida. Utilice el formato AAAA-MM-DD.")
            return render(request, "list_pdf.html", {'documentos': documentos, 'Document': Document})

        # Ahora puedes usar start_date en tus filtros
        documentos = documentos.filter(start_date=start_date)

    return render(request, "list_pdf.html", {'documentos': documentos, 'Document': Document})



