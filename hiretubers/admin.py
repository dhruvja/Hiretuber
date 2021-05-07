from django.contrib import admin
from .models import Hiretubers
# Register your models here.

class hiretuberadmin(admin.ModelAdmin):
    list_display = ('first_name','email','tuber_name')

admin.site.register(Hiretubers,hiretuberadmin)