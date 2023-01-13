from django.db import models

# Create your models here.

class Message(models.Model):
    user = models.CharField("Teacher Name", max_length = 20)
    subject = models.CharField("Major", max_length = 10)
    content = models.TextField("Comment")
    publication_date = models.DateTimeField("Time",auto_now_add=True)

    def __str__(self):
        return self.subject
    
