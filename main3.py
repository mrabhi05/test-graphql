import json
import graphene

class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.String()


class CreatePerson(graphene.Mutation):
    class Arguments:
        name = graphene.String()
    
    ok = graphene.Boolean()
    person = graphene.Field(Person)

    def mutate(self, info, name):
        person = Person(name=name)
        ok = True
        return CreatePerson(person=person, ok=ok)
    

class MyMutation(graphene.ObjectType):
    create_person = CreatePerson.Field()


class Query(graphene.ObjectType):
    person = graphene.Field(Person)

schema =  graphene.Schema(query=Query, mutation=MyMutation)
    
print(schema)


# ============== GraphQL Query ===============

query_graphql = '''
mutation myFirstMutation {
        createPerson(name:"Peter"){
        person {
            name
        }
        ok
    }

}
'''

result = schema.execute(query_graphql)
print(json.dumps(result.data, indent=3))