from django.db import models

# Create your models here.

class Contacttuber(models.Model):
    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    details = models.TextField()