# http://py4e-data.dr-chuck.net/comments_42.json
# http://py4e-data.dr-chuck.net/comments_1510110.json
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter link: ")
print("Retrieving: ", url)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print("Retrieved", len(data), "characters")

js = json.loads(data)        # parse it with json
length = len(js["comments"])

nNum = list()

for i in range(length):
    cnum = js["comments"][i]['count']
    nNum.append(cnum)
print("Sum:", sum(nNum))
