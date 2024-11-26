from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField
# from tasks.models import Review

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('moderator', 'Moderator')
    )
    roles = models.CharField(max_length=12, default='user', choices=ROLE_CHOICES)

