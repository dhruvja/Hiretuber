from django.contrib import admin
from .models import Slider , Teams, Aboutus
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="40">'.format(object.photo.url))

    list_display = ('id','myphoto','first_name','role','created_date')
    list_display_links = ('first_name',)
    list_filter = ('role',)
    search_fields = ('first_name','role')

class Slideradmin(admin.ModelAdmin):
    list_display = ('headline','subtitle','button_text')

class Aboutadmin(admin.ModelAdmin):
    list_display = ('id','heading')
    list_display_links = ('id',)

admin.site.register(Slider,Slideradmin)
admin.site.register(Teams,TeamAdmin)
admin.site.register(Aboutus,Aboutadmin)