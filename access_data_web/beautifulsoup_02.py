import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl

# Use this to ignore the SSL certificate errors  --> deal with HTTPS problem
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")      #please read this messy HTML page and give me back a structure object

#Retrieve all of the anchor tags
tags = soup("a")
for tag in tags:
    print(tag.get("href", None))
