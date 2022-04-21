from graphene import Mutation, ObjectType, String, Field, ID, Int, List, DateTime, Boolean
from graphene_django.types import DjangoObjectType
from .models import RegisteredJobs
from users.models import User
from jobs.models import Jobs

class RegisteredJobsType(DjangoObjectType):
  class Meta:
    model = RegisteredJobs

class ApplyJob(Mutation):
  job = Field(RegisteredJobsType)

  class Arguments:
    job_id = ID(required=True)

  @staticmethod
  def mutate(root, info, **kwargs):
    get_user = info.context.user
    get_job = Jobs.objects.get(id=kwargs.get('job_id'))
    if get_user.is_anonymous:
      raise Exception('Not logged in!')
    else:
      registered_job = RegisteredJobs.objects.apply_job(
        user = get_user,
        job = get_job,
        **kwargs
      )
      return ApplyJob(
        job = registered_job
      )

class Mutation(ObjectType):
  apply_job = ApplyJob.Field()