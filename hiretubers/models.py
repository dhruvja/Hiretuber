from django.db import models

# Create your models here.

class Hiretubers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    tuber_id = models.IntegerField(blank=True)
    tuber_name = models.CharField(max_length=255,blank=True)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
        