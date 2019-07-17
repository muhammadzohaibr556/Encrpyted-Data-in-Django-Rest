from django.db import models

from django_cryptography.fields import encrypt
# Create your models here.
class Personal (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    sensitive_data = encrypt(models.CharField(max_length=50, blank=True))
    
    def __str__(self):
        return self.first_name