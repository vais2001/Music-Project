from django.db import models
class Viewer(models.Model):
    viewer_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=20)
    rearrange_password=models.CharField(max_length=20)
    
    
def register(self):
    self.save()    