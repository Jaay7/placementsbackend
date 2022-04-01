from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class StudentDetailsManager(BaseUserManager):
  
  def add_details(self, student_id, full_name, education, current_cgpa, experience, skills):
    if not student_id:
      raise ValueError(_('Users must have a student_id'))
    if not full_name:
      raise ValueError(_('Users must have a full_name'))
    if not education:
      raise ValueError(_('Users must have an education'))
    if not current_cgpa:
      raise ValueError(_('Users must have a current_cgpa'))
    if not experience:
      raise ValueError(_('Users must have an experience'))
    if not skills:
      raise ValueError(_('Users must have a skills'))
    details = self.model(
      student_id=student_id,
      full_name=full_name,
      education=education,
      current_cgpa=current_cgpa,
      experience=experience,
      skills=skills
    )
    details.save()
    return details
  
  def get_details(self, student_id=None):
    if not student_id:
      raise ValueError(_('Users must have an id'))
    return self.get(student_id=student_id)