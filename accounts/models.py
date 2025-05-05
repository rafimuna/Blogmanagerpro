from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User Model তৈরি করছি
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)  # আমরা নিজে থেকে admin চিহ্নিত করবো

    def __str__(self):
        return self.username
