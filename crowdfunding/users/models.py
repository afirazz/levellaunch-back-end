from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.URLField(default="https://www.shutterstock.com/image-vector/blank-avatar-photo-place-holder-600nw-1095249842.jpg")
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username