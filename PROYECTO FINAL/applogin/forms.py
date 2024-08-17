from django import forms
from django.db import models
class Notas(models.Model):
    cuerpo = models.TextField(max_length=360)
    autor = models.CharField(max_length=30)
    areUHappy = models.BooleanField()