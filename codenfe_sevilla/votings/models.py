from django.db import models

class Voting(models.Model):
    vote = models.BooleanField()
    date = models.DateField()
    justification = models.TextField()

    def str(self):
        return f"Vote: {self.vote}, Date: {self.date}"