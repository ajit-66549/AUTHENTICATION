from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    description = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    
