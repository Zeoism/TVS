from django.db import models

# Create your models here.

class Message(models.Model):
    user = models.CharField("Name", max_length = 20)
    subject = models.CharField("Subject", max_length = 10)
    content = models.TextField("Content")
    publication_date = models.DateTimeField("Time",auto_now_add=True)

    def __str__(self):
        return self.subject

