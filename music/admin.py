from django.contrib import admin
from .models.listner import Song
from .models.viewer import Viewer
# Register your models here.
class AdminSong(admin.ModelAdmin):
    list_display=['song_name','singer','album_title']
admin.site.register(Song,AdminSong)

class AdminViewer(admin.ModelAdmin):
    list_display=['viewer_name','email','password']
admin.site.register(Viewer,AdminViewer)