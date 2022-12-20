from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('blogger-detail', kwargs={"pk": self.pk})
    