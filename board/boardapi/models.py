from django.db import models
from django.db.models.fields import AutoField

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=255, blank=False, default='')
    desc = models.TextField(blank=False, default='')
    writer = models.CharField(max_length=255, blank=False)


class Member(models.Model):
    userid = models.CharField(max_length=255, blank=False)
    password = models.CharField(max_length=255, blank=False)
