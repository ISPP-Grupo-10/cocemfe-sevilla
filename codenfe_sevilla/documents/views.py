from django.shortcuts import render
from documents.models import Document

# Create your views here.
def docsList(request):

    documentos = Document.objects.all()
    return render(request, "documents/docsList.html", {'documentos': documentos})