import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter: ")
html = urllib.request.urlopen(url).read()   # retrieve all the html
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup("a")
for tag in tags:
    print(tag.get('href', None))

# http://www.dr-chuck.com/page1.htm