import graphene
from graphql_auth.schema import MeQuery, UserQuery

import demencia_test.schema

import demencia.schema

import users.schema


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
