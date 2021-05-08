from django.db import models

# Create your models here.

class Teams(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/teams/%Y/%m/%d')
    created_date = models.DateTimeField(auto_now_add=True)
    yt_link = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name

class Aboutus(models.Model):
    heading = models.CharField(max_length=255,blank=True)
    description = models.TextField()
    photo = models.ImageField(upload_to="media/aboutus/%Y/%m")


    def __str__(self):
        return self.heading

class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length = 255)
    photo = models.ImageField(upload_to='media/slider/%y/')
    created_date = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.headline
