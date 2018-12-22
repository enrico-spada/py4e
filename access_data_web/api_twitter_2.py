import urllib.request, urllib.parse, urllib.error
from enrico.twitter import twurl
import json
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
#https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/overview

# Ignore SSL certificare errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print("")
    acct = input("Enter Twitter Account: ")
    if len(acct) < 1:
        break
    url = twurl.augment(TWITTER_URL,
                        {"screen_name": acct,
                        "count": 20}
                        )
    print("Retrieving", url)
    connection = urllib.request.urlopen(url, context = ctx)    #shut off security checking for the SSL certificare
    data = connection.read().decode()

    #There is no need to use try-except because I am sure Twitter is giving me the right stuff
    js = json.loads(data)                       #deserialize json into dictionary
    print(json.dumps(js, indent = 2))           #print json as string

    headers = dict(connection.getheaders())     #extract only headers
    print("Remaining", headers["x-rate-limit-remaining"])

    for user in js["users"]:
        print(user["screen_name"])
        if "status" not in user:                #solves exception where user has no status
            print("   * No status found")
            continue
        status = user["status"]["text"]
        print("   ", status[ : ])
