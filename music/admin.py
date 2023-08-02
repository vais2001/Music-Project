from django.contrib import admin
from .models.listner import Song
# Register your models here.
class AdminSong(admin.ModelAdmin):
    list_display=['song_name','singer','album_title']
admin.site.register(Song,AdminSong)