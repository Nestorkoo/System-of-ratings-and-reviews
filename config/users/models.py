from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField


class CustomUser(AbstractUser):
    roles_choise = [
        ('user', 'User'),
        ('admin', 'Admin')
    ]
    roles = ArrayField(
        models.CharField(max_length=12, choices=roles_choise),
        default=list,  # Використовуємо callable `list`
        blank=True
    )


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} at {self.created_at}'