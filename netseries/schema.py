import graphene

import series.schema


class Query(series.schema.Query, graphene.ObjectType):
    pass

class Mutation(series.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
