from django.db import models
from django.contrib.auth.models import User
from django_cryptography.fields import encrypt
# Create your models here.
class Personal (models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return self.email