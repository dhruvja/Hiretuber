from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Youtuber(models.Model):

    crew_choices = (
        ('solo','solo'),
        ('small','small'),
        ('large','large'),
    )

    camera_choices = (
        ('sony','sony'),
        ('nikon','nikon'),
        ('canon','canon'),
    )

    category_choices = (
        ('coding','coding'),
        ('gaming','gaming'),
        ('cooking','cooking'),
        ('comedy','comedy'),
        ('Tech reviews','Tech reviews'),
        ('Vlogs','Vlogs'),

    )


    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/ytubers/%y/%m')
    video_url = models.CharField(max_length=255)
    description = CKEditor5Field()
    city = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    height = models.IntegerField()
    crew = models.CharField(choices = crew_choices ,max_length=255)
    camera_type = models.CharField(choices = camera_choices,max_length=255)
    subs_count = models.IntegerField()
    category = models.CharField(choices = category_choices, max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)