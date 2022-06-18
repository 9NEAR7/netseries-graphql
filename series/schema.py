import graphene
from graphene_django import DjangoObjectType

from .models import Serie


class SerieType(DjangoObjectType):
    class Meta:
        model = Serie


class Query(graphene.ObjectType):
    series = graphene.List(SerieType)

    def resolve_series(self, info, **kwargs):
        return Serie.objects.all()

# ...code
#1
class CreateSerie(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    description = graphene.String()
    year = graphene.String()
    seasons = graphene.String()
    url = graphene.String()
    

    #2
    class Arguments:
        name = graphene.String()
        description = graphene.String()
        year = graphene.String()
        seasons = graphene.String()
        url = graphene.String()
        

    #3
    def mutate(self, info, name, description, year, seasons, url):
        serie = Serie(name=name, description=description, year=year, seasons=seasons, url=url)
        serie.save()

        return CreateSerie(
            id=serie.id,
            name=serie.name,
            description=serie.description,
            year=serie.year,
            seasons=serie.seasons,
            url=serie.url,
        )


#4
class Mutation(graphene.ObjectType):
    create_serie = CreateSerie.Field()
