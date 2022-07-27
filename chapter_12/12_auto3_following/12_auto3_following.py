# http://py4e-data.dr-chuck.net/known_by_Fikret.html
# http://py4e-data.dr-chuck.net/known_by_Byron.html
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
operate = int(input("How many times you want to operate: "))
pos = int(input("Enter position: "))

for i in range(operate):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    link = []   # creating a list to put all the values
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        lst = tag.get('href', None) # got all the values
        link.append(lst)    # add all the values on the list
    
    # take it out of the loop so you won't get the second value on every link
    # and you will get the whole link that you wanted
    rlink = link[pos-1]     # finding the right link; [pos-1] -> so nonprogrammers can use it
    
    if len(lst) < operate:  # if there is no more links
        break               # stop this shit
    else:
        url = rlink         # start with the next link
    print(rlink)            # print the link we want