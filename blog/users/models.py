from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')
    status = models.CharField(max_length=1000, null=False)
    bio = models.CharField(max_length=1000)
    city =  models.CharField(max_length=1000)
    gender = models.CharField(max_length=1000)
    
    
    def __str__(self):
        return f'{self.user.username} Profile'
    