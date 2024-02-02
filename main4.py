import json
import graphene

class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.String()


class PersonInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    age = graphene.String(required=True)


class CreatePerson(graphene.Mutation):
    class Arguments:
        person_data = PersonInput(required=True)
    
    person = graphene.Field(Person)

    def mutate(self, info, person_data):
        person = Person(name=person_data.name, age=person_data.age)
        return CreatePerson(person=person)
    

class MyMutation(graphene.ObjectType):
    create_person = CreatePerson.Field()


class Query(graphene.ObjectType):
    person = graphene.Field(Person)

schema =  graphene.Schema(query=Query, mutation=MyMutation)
    
print(schema)


# ============== GraphQL Query ===============

query_graphql = '''
mutation myFirstMutation {
        createPerson (personData: {name: "Peter", age: "24" }) {
            person {
                age
                name
            }
    }

}
'''

result = schema.execute(query_graphql)
print(json.dumps(result.data, indent=3))