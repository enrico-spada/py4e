import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter - ")
html = urllib.request.urlopen(url).read()   #remember .read() reads it all as one long string!
soup = BeautifulSoup(html, "html.parser")   #it returns a soup object

#Now we can query the soup object :)

# Retrieve all of the anchor tags
tags = soup("a")
for tag in tags:
    print(tag.get("href", None))
