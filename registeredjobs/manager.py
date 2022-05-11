from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class RegisteredJobsManager(BaseUserManager):

  def apply_job(self, *args, **kwargs):
    # get user and job details from models and save them
    registration = self.model(**kwargs)
    registration.save()
    return "Application sent"
  
  def get_job(self, id=None):
    if not id:
      raise ValueError(_('Jobs must have an id'))
    return self.get(pk=id)

  def remove_application(self, id=None):
    if not id:
      raise ValueError(_('Jobs must have an id'))
    else:
      registration = self.get(pk=id)
      registration.delete()
      return "Application removed"