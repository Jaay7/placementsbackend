from graphene import Float, Mutation, ObjectType, String, Field, ID, Int, List, DateTime, Boolean
from graphene_django.types import DjangoObjectType
from .models import StudentDetails
import graphql_jwt

class StudentDetailsType(DjangoObjectType):
  class Meta:
    model = StudentDetails


class Query(object):
  student_details = Field(StudentDetailsType, student_id=Int(required=True))

  #resolve student details by student id
  @staticmethod
  def resolve_student_details(self, info, **kwargs):
    student_id = kwargs.get('student_id')
    return StudentDetails.objects.get(student_id=student_id)


class AddStudentDetails(Mutation):
  student_id = Int()
  full_name = String()
  education = String()
  current_cgpa = Float()
  experience = String()
  skills = String()

  class Arguments:
    education = String(required=True)
    current_cgpa = String(required=True)
    experience = String(required=True)
    skills = String(required=True)
  
  @staticmethod
  def mutate(self, info, **kwargs):
    # verify auth token
    user = info.context.user
    if user.is_anonymous:
      raise Exception('Not logged in!')
    else:
      # get the user id
      user_id = user.id
      user_full_name = user.full_name
      student_details = StudentDetails.objects.create(
        student_id=user_id,
        student_full_name=user_full_name,
        **kwargs
      )
      return AddStudentDetails(
        student_id=student_details.student_id,
        full_name=student_details.student_full_name,
        education=student_details.education,
        current_cgpa=student_details.current_cgpa,
        experience=student_details.experience,
        skills=student_details.skills,
      )
    

class Mutation(ObjectType):
  add_student_details = AddStudentDetails.Field()