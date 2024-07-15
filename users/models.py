from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    image = models.ImageField(upload_to='users_profile_images', null=True, blank=True)
    premium_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return f"User: {self.username} | ID: {self.id}"
