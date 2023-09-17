from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=400)
    
   

