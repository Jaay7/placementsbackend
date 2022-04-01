from graphene import Mutation, ObjectType, String, Field, ID, Int, List, DateTime, Boolean
from graphene_django.types import DjangoObjectType
from .models import StudentDetails
import graphql_jwt

class StudentDetailsType(DjangoObjectType):
  class Meta:
    model = StudentDetails


class Query(object):
  student_details = Field(StudentDetailsType, student_id=String(required=True))

  @staticmethod
  def resolve_student_details(self, info, id):
    return StudentDetails.objects.get(student_id=id)


class AddStudentDetails(Mutation):
  student_details = Field(StudentDetailsType)

  class Arguments:
    student_id = String(required=True)
    full_name = String(required=True)
    education = String(required=True)
    current_cgpa = String(required=True)
    experience = String(required=True)
    skills = String(required=True)
  
  @staticmethod
  def mutate(self, info, **kwargs):
    student_details = StudentDetails.objects.create(**kwargs)
    return AddStudentDetails(student_details=student_details)

class Mutation(ObjectType):
  add_student_details = AddStudentDetails.Field()