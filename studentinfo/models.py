from djongo import models
from django.utils import timezone

from .manager import StudentDetailsManager


class StudentDetails(models.Model):
  student_id = models.IntegerField(unique=True)
  student_full_name = models.CharField(max_length=255)
  education = models.CharField(max_length=255, blank=True, null=True)
  current_cgpa = models.FloatField(blank=True, null=True)
  experience = models.CharField(max_length=255, blank=True, null=True)
  skills = models.CharField(max_length=255, blank=True, null=True)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(default=timezone.now)

  objects = StudentDetailsManager()

  def __str__(self):
    return self.student_id