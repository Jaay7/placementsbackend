from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

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