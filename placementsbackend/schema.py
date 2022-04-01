import graphene

import users.schema
import jobs.schema
import studentinfo.schema

class Query(users.schema.Query, jobs.schema.Query, studentinfo.schema.Query, graphene.ObjectType):
  pass

class Mutation(users.schema.Mutation, jobs.schema.Mutation, studentinfo.schema.Mutation, graphene.ObjectType):
  pass


schema = graphene.Schema(query=Query, mutation=Mutation)