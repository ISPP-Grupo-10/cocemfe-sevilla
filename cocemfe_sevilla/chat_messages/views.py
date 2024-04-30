from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import ChatMessage
from documents.models import Document

@login_required
def chatPage(request,pk, *args, **kwargs):
    doc = get_object_or_404(Document, id=pk)
    if request.user in doc.professionals.all() or request.user.is_staff:
        comments = ChatMessage.objects.filter(document=doc)
        return render(request, "chatPage.html", {'doc': doc, 'chat_messages': comments, 'document_id': doc.pk})
    else:
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
