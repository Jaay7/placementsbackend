from djongo import models
from django.utils import timezone

from .manager import JobManager

class Jobs(models.Model):
  company_name = models.CharField(max_length=255, unique=True)
  company_description = models.TextField(blank=True, default='')
  company_logo = models.TextField(blank=True, default='')
  company_website = models.TextField(blank=True, default='')
  company_email = models.EmailField(blank=True, default='')
  company_phone = models.CharField(max_length=255, blank=True, default='')
  company_address = models.TextField(blank=True, default='')
  company_city = models.CharField(max_length=255, blank=True, default='')
  company_state = models.CharField(max_length=255, blank=True, default='')
  job_title = models.CharField(max_length=255, blank=True, default='')
  job_description = models.TextField(blank=True, default='')
  job_requirements = models.TextField(blank=True, default='')
  job_salary = models.CharField(max_length=255, blank=True, default='')
  job_location = models.TextField(blank=True, default='')
  job_type = models.CharField(max_length=255, blank=True, default='')
  job_category = models.CharField(max_length=255, blank=True, default='')
  job_min_qualifications = models.TextField(blank=True, default='')
  job_pref_qualifications = models.TextField(blank=True, default='')
  job_experience = models.TextField(blank=True, default='')
  job_education = models.CharField(max_length=255, blank=True, default='')
  job_skills = models.TextField(blank=True, default='')
  job_start_date = models.CharField(max_length=255, blank=True, default='')
  job_created_at = models.DateTimeField(default=timezone.now)
  job_updated_at = models.DateTimeField(default=timezone.now)

  objects = JobManager()

  def __str__(self):
    return self.company_name