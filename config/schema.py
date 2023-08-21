import graphene
from graphql_auth.schema import MeQuery, UserQuery

import demencia_test.schema
import users.schema

import demencia.schema


class Query(
    demencia.schema.Query,
    UserQuery,
    MeQuery,
    graphene.ObjectType
):
    pass


class Mutation(
    demencia_test.schema.Mutation,
    users.schema.AuthMutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
