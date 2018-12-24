#This is a restartable spider
#including a many-to-many relationship
    #friends are directional relationship

import urllib.request, urllib.error, urllib.parse
from enrico.twitter import twurl
import json
import sqlite3
import ssl

TWITTER_URL = "https://api.twitter.com/1.1/friends/list.json"

conn = sqlite3.connect("db_twitter_spider_advanced.sqlite")
cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS PEOPLE
                (ID INTEGER PRIMARY KEY,
                NAME TEXT UNIQUE,
                RETRIEVED INTEGER)
            ''')
cur.execute('''
            CREATE TABLE IF NOT EXISTS FOLLOWS
                (FROM_ID INTEGER,
                TO_ID INTEGER,
                UNIQUE(FROM_ID, TO_ID)
                )
            ''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input("Enter a Twitter account, or quit: ")
    if acct == "quit":
        break
    if len(acct) < 1:
        cur.execute('SELECT ID, NAME FROM PEOPLE WHERE RETRIEVED = 0 LIMIT 1')
        try:
            (id, acct) = cur.fetchone()
        except:
            print("No unretrieved Twitter accounts found")
            continue
    else:
        #check if the account name in Input is already in the DB
        cur.execute('SELECT ID FROM PEOPLE WHERE NAME = ? LIMIT 1',
                    (acct, )
                    )
        try:
            id = cur.fetchone()[0]
        except:
            cur.execute('''
                        INSERT OR IGNORE INTO PEOPLE (NAME, RETRIEVED)
                        VALUES
                        (?, 0)''',
                        (acct, )
                        )
            conn.commit()
            if cur.rowcount != 1:         #how many rows were affected?
                print("Error inserting account:", acct)
                continue
            id = cur.lastrowid      #grab the PK assigned by SQL

        #at this point we either know the id of the user that was there before
        #or we inserted one and know its PK

    url = twurl.augment(TWITTER_URL, {"screen_name": acct, "count": 200})
    print("Retrieving account", acct)
    try:
        connection = urllib.request.urlopen(url, context = ctx)
    except Exception as err:
        print("Requests limit exceeded. Failed to Retrieve.\n", err)
        break
    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print("Remaning", headers["x-rate-limit-remaining"])

    try:
        js = json.loads(data)       #parse the data into a list of lists
    except:
        print("Unable to parse json")
        print(data)
        break           #we could also continue, but if the Json blowed-up that bad, we should quit

    #Debugging
    #print(json.dumps(js, indent = 2))

    if "users" not in js:       #if user is not in the parsed outer dictionary (the main list)
        print("Incorrect JSON received")
        print(json.dumps(js, indent = 2))
        continue

    cur.execute("UPDATE PEOPLE SET RETRIEVED = 1 WHERE NAME = ?",
                (acct, )
                )

    #Now write a loop that goes through all the friends of acct,
    #and then check to see if each of them is already present in the db

    countnew = 0
    countold = 0
    for user in js["users"]:
        friend = user["screen_name"]
        print(friend)
        #now we try to see if friend is already in DB
        cur.execute("SELECT ID FROM PEOPLE WHERE NAME = ? LIMIT 1",
                    (friend, )
                    )
        try:
            friend_id = cur.fetchone()[0]
            countold = countold + 1
        except:
            cur.execute('''
                        INSERT OR IGNORE INTO PEOPLE (NAME, RETRIEVED)
                        VALUES
                        (?, 0)
                        ''',
                        (friend, )
                        )
            conn.commit()
            if cur.rowcount != 1:       #how many rows were affected by the last transaction?
                print("Error inserting account: ", friend)
                continue
            friend_id = cur.lastrowid
            countnew = countnew + 1

        #now we insert into the FOLLOWS (bridge table)
        cur.execute('''
                    INSERT OR IGNORE INTO FOLLOWS (FROM_ID, TO_ID)
                    VALUES
                    (?, ?)
                    ''',
                    (id, friend_id)
                    )
    print("New accounts =", countnew, " revisited = ", countold)
    conn.commit()
    print("Remaning", headers["x-rate-limit-remaining"])
cur.close()
