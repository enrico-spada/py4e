import urllib.request
from bs4 import BeautifulSoup
import ssl

# Use this to ignore the SSL certificate errors  --> deal with HTTPS problem
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# URL = input("Enter - ")
URL = "https://it.wikipedia.org/wiki/Gargano"
html = urllib.request.urlopen(URL)
soup = BeautifulSoup(html, "html.parser")

paragraphs = soup("p")
count = 0
for tag in paragraphs:
    count += 1

print("Done", count)
