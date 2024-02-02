import json
import graphene



DATA = [
    {
        "name": "Abhishek",
        "age": "25"
    },
    {
        "name": "Abhinav",
        "age": "20"
    }
]

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


class Query(graphene.ObjectType):
    array = graphene.List(Person, size = graphene.Int(default_value=1))

    def resolve_array(root, info, size):
        return DATA[:size]
    

schema =  graphene.Schema(query=Query)

# print(schema)



# ============== GraphQL Query ===============

query_graphql = '''
query myquery {
    array (size : 2) { 
        name
        age
    }
}
'''

result = schema.execute(query_graphql)
print(json.dumps(result.data, indent=3))