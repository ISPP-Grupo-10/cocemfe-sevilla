from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Voting
from suggestions.models import Suggestion
from datetime import date

def voting_vote(request, suggestion_id):
    if request.method == 'POST':
        suggestion = get_object_or_404(Suggestion, id=suggestion_id)
        existing_vote = Voting.objects.filter(suggestion=suggestion, professional=request.user).first()
        vote = request.POST.get('vote')
        justification = request.POST.get('justificacion')
        document_id = suggestion.document_id
        if existing_vote:
            # Si el usuario ya votó, actualizar el voto existente
            existing_vote.vote = vote
            existing_vote.justification = justification
            existing_vote.save()
            messages.success(request, 'Voto actualizado exitosamente.')
        else:
            # Si el usuario no ha votado aún, crear un nuevo voto
            new_vote = Voting.objects.create(
                vote=vote,
                date=date.today(),
                justification=justification,
                professional=request.user,
                suggestion=suggestion
            )
            messages.success(request, 'Voto registrado exitosamente.')
        return redirect('view_pdf_admin', pk=document_id)
    else:
        # Si no es una solicitud POST, redirigir a la vista de sugerencias
        suggestion = get_object_or_404(Suggestion, id=suggestion_id)
        return render(request, 'view_suggestion.html', {'suggestion': suggestion})