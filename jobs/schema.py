from graphene import Mutation, ObjectType, String, Field, ID, Int, List, DateTime, Boolean
from graphene_django.types import DjangoObjectType
from .models import Jobs
import graphql_jwt

class JobsType(DjangoObjectType):
  class Meta:
    model = Jobs

class Query(object):
  jobs = Field(List(JobsType))
  job = Field(JobsType, id=ID(required=True))

  @staticmethod
  def resolve_jobs(self, info, **kwargs):
    return Jobs.objects.all()

  @staticmethod
  def resolve_job(self, info, id=None):
    if not id:
      raise ValueError('Jobs must have an id')
    return Jobs.objects.get(pk=id)

class AddJob(Mutation):
  job = Field(JobsType)

  class Arguments:
    company_name = String(required=True)
    company_description = String(required=True)
    company_logo = String(required=True)
    company_website = String(required=True)
    company_email = String(required=True)
    company_phone = String(required=True)
    company_address = String(required=True)
    company_city = String(required=True)
    company_state = String(required=True)
    job_title = String(required=True)
    job_description = String(required=True)
    job_requirements = String(required=True)
    job_salary = String(required=True)
    job_location = String(required=True)
    job_type = String(required=True)
    job_category = String(required=True)
    job_experience = String(required=True)
    job_education = String(required=True)
    job_skills = String(required=True)
    job_created_at = DateTime(required=True)
    job_updated_at = DateTime(required=True)

  @staticmethod
  def mutate(root, info, **kwargs):
    job = Jobs.objects.add_job(**kwargs)
    return AddJob(
      job=job
    )

class Mutation(ObjectType):
  add_job = AddJob.Field()