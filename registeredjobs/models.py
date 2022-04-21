from djongo import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .manager import RegisteredJobsManager
from users.models import User
from jobs.models import Jobs

class RegisteredJobs(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(default=timezone.now)

  objects = RegisteredJobsManager()

  def __str__(self):
    return self.user.username