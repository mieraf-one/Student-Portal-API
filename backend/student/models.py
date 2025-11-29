from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female')
    ]

    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin')
    ]

    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    role = models.CharField(choices=ROLE_CHOICES, max_length=10)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'
