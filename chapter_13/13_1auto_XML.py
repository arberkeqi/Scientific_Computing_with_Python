import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter link address: ")
print("Retrieving", url)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()        # data here place the role of input down here
print("Retrieved", len(data), "characters")
# print(data.decode())

tree = ET.fromstring(data)
# need to create the path
results = tree.findall("comments/comment")
newNum = list()

for num in results:
    cnum = int(num.find("count").text)
    newNum.append(cnum)
print("Sum:", sum(newNum))


# import xml.etree.ElementTree as ET
# input = '''<stuff>
#     <users>
#         <user x="2">
#             <id>001</id>
#             <name>Chuck</name>
#         </user>
#         <user x="7">
#             <id>009</id>
#             <name>Brent</name>
#         </user>
#     </users>
# </stuff>'''

# stuff = ET.fromstring(input)
# lst = stuff.findall('users/user')
# print('User count:', len(lst))
# for item in lst:
#     id = int(item.find('id').text)
#     print('Name', item.find('name').text)
#     print('Id', id)
#     print('Attribute', item.get("x"))
#     print("ID type: ", type(id))