from django.db import models

# Create your models here.

class Testdjango(models.Model):
    username = models.CharField(max_length=255, blank=True, default='')
    password = models.CharField(max_length=255, blank=True, default='')

    