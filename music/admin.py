from django.contrib import admin
from .models.listner import Song,Watch_later
from .models.viewer import Viewer
# Register your models here.
class AdminSong(admin.ModelAdmin):
    list_display=['song_name','singer','album_title']
admin.site.register(Song,AdminSong)

class AdminViewer(admin.ModelAdmin):
    list_display=['user_name','first_name','last_name','phone','email','password','rearrange_password']
admin.site.register(Viewer,AdminViewer)


admin.site.register(Watch_later)