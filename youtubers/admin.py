from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html
# Register your models here.

class YoutuberAdmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src="{}" width="40">',format(object.photo.url))

    list_display = ('id','name','myphoto','price','category','is_featured')
    list_filter = ('category','crew','camera_type')
    list_editable = ('is_featured',)

admin.site.register(Youtuber,YoutuberAdmin)