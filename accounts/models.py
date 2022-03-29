# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

# GENDER_CHOICES = (
#     ('M', 'Male'),
#     ('F', 'Female')
# )

# Create your models here.


class CustomUser(AbstractUser):
    pass
    # phone = models.CharField(max_length=16)
    # gender = models.ChoiceField(choices=GENDER_CHOICES, widget=models.RadioSelect())
