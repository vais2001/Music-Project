from django.db import models

# Create your models here.
class Song(models.Model):
    song_id=models.AutoField(primary_key=True)
    song=models.FileField(upload_to='uploads',default="")
    song_name=models.CharField(max_length=100,default=None)
    singer=models.CharField(max_length=200)
    album_title=models.CharField(max_length=500)
    album_picture=models.ImageField(upload_to='uploads', default=False) 
    
    
def __str__(self):
    return self.song_name    
def __str__(self):
    return self.singer