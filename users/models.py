from djongo import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(unique=True)
  username = models.CharField(max_length=255, unique=True)
  full_name = models.CharField(max_length=255)
  profile_pic = models.TextField(blank=True, null=True)
  bio = models.TextField(blank=True, null=True)
  dob = models.DateField(blank=True, null=True)
  mobile = models.CharField(max_length=255, blank=True, null=True)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(default=timezone.now)

  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['email', 'full_name']

  objects = UserManager()

  def __str__(self):
    return self.username