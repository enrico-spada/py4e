from urllib.request import urlopen
import urllib.error
from enrico.twitter import twurl
import json
import sqlite3
import ssl          #Python does not trust any certificate no matter how good they are!

TWITTER_URL = "https://api.twitter.com/1.1/friends/list.json"

conn = sqlite3.connect("db_twitter_spider_basic.sqlite")
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS TWITTER
(NAME TEXT, RETRIEVED INTEGER, FRIENDS INTEGER)
''')

# Ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input("Enter a Twitter account name, or quit: ")
    if acct == "quit":
        break
    if len(acct) < 1:    #if no name is entered, use one name in the DB
        cur.execute('SELECT NAME FROM TWITTER WHERE RETRIEVED = 0 LIMIT 1')     #get only one row from the DB
        try:
            acct = cur.fetchone()[0]
        except:
            print("No unretrieved Twitter accounts found")
            continue

    url = twurl.augment(TWITTER_URL, {"screen_name": acct, "count": '200'})
    print("Retrieving", url)
    connection = urlopen(url, context = ctx)
    data = connection.read().decode()

    headers = dict(connection.getheaders())        #remember Twitter API returns only headers

    print("Remaining", headers["x-rate-limit-remaining"])
    js = json.loads(data)     #convert json into a list of dictionaries
    #Debugging
    #print json.dumps(js, indent = 2)  (MAYBE: is the same as js.dumps(indent = 2) ??)


    cur.execute('UPDATE TWITTER SET RETRIEVED = 1 WHERE NAME = ?',
                (acct, )
                )

    countnew = 0
    countold = 0
    for user in js["users"]:
        friend = user["screen_name"]
        print(friend)
        cur.execute('SELECT FRIENDS FROM TWITTER WHERE NAME = ? LIMIT 1',
                    (friend, )
                    )
        try:
            count = cur.fetchone()
            cur.execute('UPDATE TWITTER SET FRIENDS = ? WHERE NAME = ?',
                        (count + 1, friend))
            countold = countold + 1

        except:
            cur.execute('''INSERT INTO TWITTER (NAME, RETRIEVED, FRIENDS)
                        VALUES (?, 0, 1)''',
                        (friend, )
                        )
            countnew = countnew + 1
    print("New accounts =", countnew, " revisited =", countold)
    conn.commit()

cur.close()
