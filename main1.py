import json
import graphene


class Query(graphene.ObjectType):
    name = graphene.String(value = graphene.String(default_value="Sam"))
    age = graphene.String()

    def resolve_name(root, info, value):
        return value
    
    def resolve_age(root, info):
        return "24"
    

schema = graphene.Schema(query=Query)
print(schema)

# ============= GraphQL Queries =================

query_graphql = '''
query myquery {
        myname: name (value: "Abhishek Nair")
        myage: age
}
'''

result  = schema.execute(query_graphql)
print(json.dumps(result.data, indent=3))