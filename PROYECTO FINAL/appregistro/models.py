from django.db import models

class Account(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
