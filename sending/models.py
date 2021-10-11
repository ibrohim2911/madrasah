from django.db import models
from django.contrib.auth.models import AbstractUser
class signupUser(AbstractUser):
    number = models.PositiveIntegerField(null=True, blank=True)
