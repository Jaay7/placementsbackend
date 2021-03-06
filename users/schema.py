from graphene import Mutation, ObjectType, String, Field, ID, Int, List, DateTime, Boolean
from graphene_django.types import DjangoObjectType
from .models import User
import graphql_jwt
from graphql_jwt.shortcuts import get_token

class UserType(DjangoObjectType):
  class Meta:
    model = User
    # fields = (
    #   'id',
    #   'username',
    #   'email',
    #   'full_name',
    #   'profile_pic',
    #   'bio',
    #   'dob',
    #   'mobile',
    #   'is_active',
    #   'created_at',
    #   'updated_at',
    # )

class Query(object):
  user = Field(UserType, id=ID(required=True))
  users = List(UserType)
  me = Field(UserType)

  @staticmethod
  def resolve_user(self, info, id):
    return User.objects.get(id=id)

  @staticmethod
  def resolve_users(self, info):
    return User.objects.all()

  @staticmethod
  def resolve_me(self, info):
    user = info.context.user
    if user.is_anonymous:
      raise Exception('Not logged in!')
    return user

class RegisterUser(Mutation):
  user = Field(UserType)
  token = String()

  class Arguments:
    username = String(required=True)
    email = String(required=True)
    password = String(required=True)
    full_name = String(required=True)
    profile_pic = String()
    bio = String()
    dob = DateTime()
    mobile = String()

  @staticmethod
  def mutate(self, info, **kwargs):
    user = User.objects.register_user(**kwargs)
    # user.save()
    return RegisterUser(
      user=user,
      token=get_token(user),
    )

class LoginUser(Mutation):
  username = String()
  password = String()

  class Arguments:
    username = String(required=True)
    password = String(required=True)

  @staticmethod
  def mutate(_, info, **kwargs):
    user = User.objects.login_user(
      username=kwargs.get('username'),
      password=kwargs.get('password')
    )
    return LoginUser(
      username=user.username,
      password=user.password,
    )

class SaveJob(Mutation):
  # job = Field(JobsType)
  response = String()

  class Arguments:
    job_id = ID(required=True)

  @staticmethod
  def mutate(self, info, **kwargs):
    user = info.context.user
    if user.is_anonymous:
      raise Exception('Not logged in!')
    else:
      User.objects.save_job(user_id = user.id, job_id = kwargs.get('job_id'))
      return SaveJob( response = "Job saved" )

class RemoveSavedJob(Mutation):
  # job = Field(JobsType)
  response = String()

  class Arguments:
    job_id = ID(required=True)

  @staticmethod
  def mutate(self, info, **kwargs):
    user = info.context.user
    if user.is_anonymous:
      raise Exception('Not logged in!')
    else:
      User.objects.remove_saved_job(user_id = user.id, job_id = kwargs.get('job_id'))
      return RemoveSavedJob( response = "Job removed" )

class ApplyJob(Mutation):
  # job = Field(JobsType)
  response = String()

  class Arguments:
    job_id = ID(required=True)

  @staticmethod
  def mutate(self, info, **kwargs):
    user = info.context.user
    if user.is_anonymous:
      raise Exception('Not logged in!')
    else:
      User.objects.apply_job(user_id = user.id, job_id = kwargs.get('job_id'))
      return ApplyJob( response = "Job applied" )

class RemoveAppliedJob(Mutation):
  # job = Field(JobsType)
  response = String()

  class Arguments:
    job_id = ID(required=True)

  @staticmethod
  def mutate(self, info, **kwargs):
    user = info.context.user
    if user.is_anonymous:
      raise Exception('Not logged in!')
    else:
      User.objects.remove_applied_job(user_id = user.id, job_id = kwargs.get('job_id'))
      return RemoveAppliedJob( response = "Job removed" )

class Mutation(ObjectType):
  register_user = RegisterUser.Field()
  login = graphql_jwt.ObtainJSONWebToken.Field()
  verify_token = graphql_jwt.Verify.Field()
  refresh_token = graphql_jwt.Refresh.Field()
  save_job = SaveJob.Field()
  remove_saved_job = RemoveSavedJob.Field()
  apply_job = ApplyJob.Field()
  remove_applied_job = RemoveAppliedJob.Field()