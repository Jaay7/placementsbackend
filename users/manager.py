from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

from jobs.models import Jobs

class UserManager(BaseUserManager):

  def create_superuser(self, username, email, password, **fields):

    fields.setdefault('is_superuser', True)

    if fields.get('is_superuser') is not True:
      raise ValueError(_('Superuser must have is_superuser=True'))
    
    return self.register_user(username, email, password, **fields)

  def register_user(self, username, email, password, **fields):
    if not username:
      raise ValueError(_('Users must have a username'))

    user = self.model(
      username=username,
      email=self.normalize_email(email),
      **fields
    )

    user.set_password(password)
    user.save()
    return user

  def login_user(self, username, password):
    #check if user exists and check if password matches
    user = self.get(username=username)
    if user.check_password(password):
      return user
    return None
  
  def get_user(self, id=None):
    if not id:
      raise ValueError(_('Users must have an id'))
    return self.get(pk=id)
  
  def save_job(self, user_id=None, job_id=None):
    # save the job to the user's saved_jobs many to many field
    if not job_id:
      raise ValueError(_('Jobs must have an id'))
    else:
      user = self.get(pk=user_id)
      job = Jobs.objects.get(pk=job_id)
      user.saved_jobs.add(job)
      job.saved_by.add(user)
      return "Job saved"
  
  def get_saved_jobs(self, user_id=None):
    # get the user's saved_jobs from the jobs model
    if not user_id:
      raise ValueError(_('Users must have an id'))
    else:
      user = self.get(pk=user_id)
      return user.saved_jobs.all()
  
  def remove_saved_job(self, user_id=None, job_id=None):
    # remove the job from the user's saved_jobs many to many field
    if not job_id:
      raise ValueError(_('Jobs must have an id'))
    else:
      user = self.get(pk=user_id)
      job = Jobs.objects.get(pk=job_id)
      user.saved_jobs.remove(job)
      job.saved_by.remove(user)
      return "Job removed"
  
  def apply_job(self, user_id=None, job_id=None):
    # save the job to the user's applied_jobs many to many field
    if not job_id:
      raise ValueError(_('Jobs must have an id'))
    else:
      user = self.get(pk=user_id)
      job = Jobs.objects.get(pk=job_id)
      if job not in user.applied_jobs.all():
        user.applied_jobs.add(job)
        job.applied_by.add(user)
        return "Job applied"
      else:
        return "You have already applied for this job"
  
  def remove_applied_job(self, user_id=None, job_id=None):
    # remove the job from the user's applied_jobs many to many field
    if not job_id:
      raise ValueError(_('Jobs must have an id'))
    else:
      user = self.get(pk=user_id)
      job = Jobs.objects.get(pk=job_id)
      # check if exist
      if job in user.applied_jobs.all():
        user.applied_jobs.remove(job)
        job.applied_by.remove(user)
        return "Job removed"
      else:
        return "You haven't applied for this job"
