from django.db import models
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    image = models.ImageField(upload_to='users_profile_images', null=True, blank=True)
    premium_status = models.BooleanField(default=False)
    phone = PhoneNumberField(default="+995-000-000-000", null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"User: {self.username} | ID: {self.id}"
