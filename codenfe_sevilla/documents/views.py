from django.shortcuts import render
from documents.models import Document

# Create your views here.
def docsList(request):


    return render(request, "documents/docsList.html")