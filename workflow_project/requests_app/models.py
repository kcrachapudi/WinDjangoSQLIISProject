from django.db import models

# Create your models here.

class Request(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, default='Not Started')

    def __str__(self):
        return self.title