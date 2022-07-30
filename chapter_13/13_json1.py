# python processing some json
import json

# data = '''{
#     "name : "Chuck",
#     "phone" : {
#         "type" : "intl"
#         "number" : "+1 734 303 4456"
#     },
#     "email" : {
#         "hide" : "yes"
#     }
# }'''

# info = json.loads(data) # loads -> load from string
# print('Name:', info["name"])
# print('Hide:', info["email"]["hide"])

# Another Example

input = '''[
    { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
    },
    { id" : "009",
    "x" : "7",
    "name" : "Chuck"
    }
}'''

info  = json.loads(input)
print("User count:", len(info))
for item in info:
    print("Name", item["name"])
    print("ID", item['id'])
    print("Attribute", item['x'])