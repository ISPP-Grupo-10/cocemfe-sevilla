from django.db import models

class Suggestion(models.Model):
    main = models.CharField(max_length=255)
    justification = models.TextField()
    section = models.CharField(max_length=10)
    page = models.IntegerField()
    date = models.DateField()

    def str(self):
        return self.main