from graphene import Mutation, ObjectType, String, Field, ID, Int, List, DateTime, Boolean
from graphene_django.types import DjangoObjectType
from .models import Jobs

class JobsType(DjangoObjectType):
  class Meta:
    model = Jobs

class Query(object):
  jobs = Field(List(JobsType))
  job = Field(JobsType, id=ID(required=True))
  user_saved_jobs = List(JobsType)
  user_applied_jobs = List(JobsType)

  @staticmethod
  def resolve_jobs(self, info, **kwargs):
    return Jobs.objects.all()

  @staticmethod
  def resolve_job(self, info, id=None):
    if not id:
      raise ValueError('Jobs must have an id')
    return Jobs.objects.get(pk=id)

  @staticmethod
  def resolve_user_saved_jobs(self, info, **kwargs):
    user = info.context.user
    if user.is_anonymous:
      raise Exception('Not logged in!')
    else:
      return user.saved_jobs.all()
  
  @staticmethod
  def resolve_user_applied_jobs(self, info, **kwargs):
    user = info.context.user
    if user.is_anonymous:
      raise Exception('Not logged in!')
    else:
      return user.applied_jobs.all()

class AddJob(Mutation):
  job = Field(JobsType)

  class Arguments:
    company_name = String(required=True)
    company_description = String(required=True)
    company_logo = String()
    company_website = String(required=True)
    company_email = String()
    company_phone = String()
    company_address = String(required=True)
    company_city = String()
    company_state = String()
    job_title = String(required=True)
    job_description = String(required=True)
    job_requirements = String(required=True)
    job_salary = String()
    job_location = String(required=True)
    job_type = String()
    job_category = String()
    job_min_qualifications = String()
    job_pref_qualifications = String()
    job_experience = String()
    job_education = String()
    job_skills = String()
    job_start_date = String()
    job_created_at = DateTime()
    job_updated_at = DateTime()

  @staticmethod
  def mutate(root, info, **kwargs):
    job = Jobs.objects.add_job(**kwargs)
    return AddJob(
      job=job
    )

class Mutation(ObjectType):
  add_job = AddJob.Field()