from django.db import models
class Viewer(models.Model):
    user_name=models.CharField(max_length=200, null=True, blank=True)
    first_name=models.CharField(max_length=200, null=True, blank=True)
    last_name=models.CharField(max_length=200, null=True, blank=True)
    phone=models.CharField(max_length=10, null=True, blank=True)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=20, null=True, blank=True)
    rearrange_password=models.CharField(max_length=20, null=True, blank=True)
    
    
def register(self):
    self.save()    