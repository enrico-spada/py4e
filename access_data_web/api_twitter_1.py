import urllib.request, urllib.parse, urllib.error
from enrico.twitter import twurl
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
#https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.html


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print("")
    acct = input("Enter Twitter Account: ")
    if len(acct) < 1: break
    url = twurl.augment(TWITTER_URL,
                        {"screen_name": acct,
                        "count": "2"})
    print("Retrieving", url)
    connection = urllib.request.urlopen(url, context = ctx)
    data = connection.read().decode()
    print(data[ : 250])
    headers = dict
    headers = dict(connection.getheaders())    #usually urllib returns the body, Twitter API sends back only headers ;)
    print(headers)
    print("Remaining", headers["x-rate-limit-remaining"])
