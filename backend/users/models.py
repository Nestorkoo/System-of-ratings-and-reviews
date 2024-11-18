from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField
# from tasks.models import Review

class CustomUser(AbstractUser):
    roles_choise = [
        ('user', 'User'),
        ('admin', "Admin"),
    ]
    roles = models.CharField(max_length=12, default='user', choices=roles_choise)

