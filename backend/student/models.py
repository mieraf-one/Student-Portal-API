from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female')
    ]

    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)