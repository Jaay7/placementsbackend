from graphene import Mutation, ObjectType, String, Field, ID, Int, List, DateTime, Boolean
from graphene_django.types import DjangoObjectType
from .models import RegisteredJobs
from users.models import User
from jobs.models import Jobs

class RegisteredJobsType(DjangoObjectType):
  class Meta:
    model = RegisteredJobs

class Query(object):
  registered_jobs = List(RegisteredJobsType)
  #resolve registered jobs by job id
  @staticmethod
  def resolve_registered_jobs(self, info, **kwargs):
    user = info.context.user
    if user.is_anonymous:
      raise Exception('Not logged in!')
    else:
      # job_id = kwargs.get('job_id')
      return RegisteredJobs.objects.filter(user=user.id)

class ApplyJob(Mutation):
  response = String()

  class Arguments:
    job_id = ID(required=True)

  @staticmethod
  def mutate(root, info, **kwargs):
    get_user = info.context.user
    get_job = Jobs.objects.get(id=kwargs.get('job_id'))
    if get_user.is_anonymous:
      raise Exception('Not logged in!')
    else:
      RegisteredJobs.objects.apply_job(
        user = get_user,
        job = get_job,
        **kwargs
      )
      return ApplyJob(
        response = "Application sent"
      )

class RemoveApplication(Mutation):
  response = String()

  class Arguments:
    apl_id = ID(required=True)

  @staticmethod
  def mutate(root, info, **kwargs):
    get_user = info.context.user
    if get_user.is_anonymous:
      raise Exception('Not logged in!')
    else:
      RegisteredJobs.objects.remove_application(
        id = kwargs.get('apl_id')
      )
      return RemoveApplication(
        response = "Application removed"
      )


class Mutation(ObjectType):
  apply_job = ApplyJob.Field()
  remove_application = RemoveApplication.Field()