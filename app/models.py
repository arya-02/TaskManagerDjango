from django.db import models

# Create your models here.

class Tasks(models.Model):
    content = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)