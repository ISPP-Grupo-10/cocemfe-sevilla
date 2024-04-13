from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from documents.models import Document
from suggestions.models import Suggestion
from datetime import date
from .models import Voting

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
            new_vote = Voting.objects.create(
                vote=vote,
                date=date.today(),
                justification=justification,
                professional=request.user,
                suggestion=suggestion
            )
            new_vote = new_vote
            messages.success(request, 'Voto registrado exitosamente.')
        return redirect('view_pdf_admin', pk=document_id)
    else:
        # Si no es una solicitud POST, redirigir a la vista de sugerencias
        suggestion = get_object_or_404(Suggestion, id=suggestion_id)
        return render(request, 'view_suggestion.html', {'suggestion': suggestion})
    
    
def voting_statistics(request, pk):
    document = Document.objects.get(pk=pk)
    suggestions = Suggestion.objects.filter(document=document)
    
    suggestion_data = []
    for suggestion in suggestions:
        votes = Voting.objects.filter(suggestion=suggestion)
        votes_agree = votes.filter(vote=True).count()
        votes_disagree = votes.filter(vote=False).count()
        
        professionals_voted = set(vote.professional for vote in votes)
        professionals_remaining = document.professionals.exclude(id__in=[prof.id for prof in professionals_voted]).count()
        
        suggestion_data.append({
            'suggestion': suggestion,
            'votes_agree': votes_agree,
            'votes_disagree': votes_disagree,
            'professionals_remaining': professionals_remaining,
        })
    
    context = {
        'document': document,
        'suggestion_data': suggestion_data,
    }
    
    return render(request, 'voting_statistics.html', context)