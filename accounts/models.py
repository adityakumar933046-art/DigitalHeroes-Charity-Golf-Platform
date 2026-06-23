from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_image = models.ImageField(
    upload_to='profiles/',
    blank=True,
    null=True
)


    def __str__(self):
        return self.username