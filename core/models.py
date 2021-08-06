from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class UserLoginHistory(models.Model):
    dateCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dateModified = models.DateTimeField(null=True, blank=True, default=timezone.now)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ip = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.ip)
    