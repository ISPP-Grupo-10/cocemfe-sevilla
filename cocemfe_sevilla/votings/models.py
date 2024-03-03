from django.db import models
from professionals.models import Professional
from suggestions.models import Suggestion

class Voting(models.Model):
    vote = models.BooleanField()
    date = models.DateField()
    justification = models.TextField()
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, null=True, related_name='votings')
    suggestion= models.ForeignKey(Suggestion, on_delete=models.CASCADE, null=True, related_name='votings')

    def __str__(self):
        return f"Vote: {self.vote}, Date: {self.date}"