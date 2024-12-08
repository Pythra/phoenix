from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser): 
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True) 
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username