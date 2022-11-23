from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length=128, blank=True, null=True)
    MBTI_type = models.CharField(max_length=4, blank=True, null=True)
    
    def __str__(self):
        return self.username
