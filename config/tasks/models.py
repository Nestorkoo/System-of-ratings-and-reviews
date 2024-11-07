from django.db import models
from users.models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()
class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    username = models.CharField(max_length=150, editable=False, null=True, blank=True)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Review by {self.user.username} at {self.created_at}'