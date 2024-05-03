from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from professionals.models import Professional

from .models import ChatMessage
from documents.models import Document

@login_required
def chatPage(request,pk, *args, **kwargs):
    doc = get_object_or_404(Document, id=pk)
    if request.user in doc.professionals.all() or request.user.is_staff:
        comments = ChatMessage.objects.filter(document=doc)
        professional = Professional.objects.filter(username=request.user.username).get()
        if professional.profile_picture != "":
            profile_picture = "/media/" + str(professional.profile_picture)
        else:
            profile_picture = "/media/IconoUsuario.jpg"
        return render(request, "chatPage.html", {'doc': doc, 'chat_messages': comments, 'document_id': doc.pk, 'picture': profile_picture})
    else:
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
