# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

# Create your models here.


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=16, default='')
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.IntegerField(choices=GENDER_CHOICES, default='')
    STATUS_PARTICULIER = 0
    STATUS_ENTREPRISE = 1
    STATUS_CHOICES = [(STATUS_PARTICULIER , 'particulier'), (STATUS_ENTREPRISE, 'entreprise')]
    status = models.IntegerField(choices=STATUS_CHOICES, default='')
