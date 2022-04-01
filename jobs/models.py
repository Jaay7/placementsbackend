from djongo import models
from django.utils import timezone

from .manager import JobManager

class Jobs(models.Model):
  company_name = models.CharField(max_length=255, unique=True)
  company_description = models.TextField(blank=True, null=True)
  company_logo = models.TextField(blank=True, null=True)
  company_website = models.TextField(blank=True, null=True)
  company_email = models.EmailField(blank=True, null=True)
  company_phone = models.CharField(max_length=255, blank=True, null=True)
  company_address = models.TextField(blank=True, null=True)
  company_city = models.CharField(max_length=255, blank=True, null=True)
  company_state = models.CharField(max_length=255, blank=True, null=True)
  job_title = models.CharField(max_length=255, blank=True, null=True)
  job_description = models.TextField(blank=True, null=True)
  job_requirements = models.TextField(blank=True, null=True)
  job_salary = models.CharField(max_length=255, blank=True, null=True)
  job_location = models.CharField(max_length=255, blank=True, null=True)
  job_type = models.CharField(max_length=255, blank=True, null=True)
  job_category = models.CharField(max_length=255, blank=True, null=True)
  job_experience = models.CharField(max_length=255, blank=True, null=True)
  job_education = models.CharField(max_length=255, blank=True, null=True)
  job_skills = models.TextField(blank=True, null=True)
  job_created_at = models.DateTimeField(default=timezone.now)
  job_updated_at = models.DateTimeField(default=timezone.now)

  objects = JobManager()

  def __str__(self):
    return self.company_name