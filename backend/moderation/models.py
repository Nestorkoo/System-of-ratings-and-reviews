from django.db import models
from users.models import CustomUser
from tasks.models import Review

class Reports(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='reports')
    reason = models.CharField()
    resolved = models.BooleanField(default=False)
    reported_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'Report on Review ID {self.review.id} by {self.reported_by.username}'
    