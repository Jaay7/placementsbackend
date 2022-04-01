from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class JobManager(BaseUserManager):

  def add_job(self, *args, **kwargs):
    job = self.model(**kwargs)
    job.save()
    return job
  
  def get_job(self, id=None):
    if not id:
      raise ValueError(_('Jobs must have an id'))
    return self.get(pk=id)