from bs4 import BeautifulSoup
import sqlite3
import urllib.error
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
import re
import ssl

# Ignore SSL Certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect("db_spider.sqlite")
cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS PAGES
            (ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            URL TEXT UNIQUE,
            HTML TEXT,
            ERROR INTEGER,
            OLD_RANK REAL,
            NEW_RANK REAL)
            ''')

#Many-to-Many table
cur.execute('''
            CREATE TABLE IF NOT EXISTS LINKS
            (FROM_ID INTEGER,
            TO_ID INTEGER)
            ''')

cur.execute('''
            CREATE TABLE IF NOT EXISTS WEBS
            (URL TEXT UNIQUE)
            ''')


#Find which pages are not yet retrieved
cur.execute('''
            SELECT  ID, URL
            FROM    PAGES
            WHERE   HTML IS NULL
                    AND ERROR IS NULL
                    AND (ID < 100 OR ID > 91271)
            ORDER BY RANDOM()
            LIMIT 1
            ''')
#HTML is NULL means the page has not yet been retrieved

row = cur.fetchone()
try:
    fromid, starturl = row[0],  row[1]
    print(fromid, starturl)
except:
    print("Starting new crawl")

if row is not None:
    print(f"Restarting existing crawl using {starturl}.\nRemove db_spider.sqlite to start a fresh crawl.")
else:
    starturl = input("Enter web url: ")
    if len(starturl) < 1:
        starturl = "https://en.wikipedia.org/wiki/Data_science"
    web = re.findall("\S+://.+?/", starturl)[0]
    print(type(web))
    print("The web parsed from input is: ", web)

    if len(web) > 1:
        cur.execute('INSERT OR IGNORE INTO WEBS (URL) VALUES (?)', (web, ) )
        cur.execute('INSERT OR IGNORE INTO PAGES (URL, HTML, NEW_RANK) VALUES (?, NULL, 1.0)', (starturl, ) )
        conn.commit()

#Get the current webs and get links only on this website
cur.execute("SELECT URL FROM WEBS")
webs = list()
for row in cur:
    webs.append(str(row[0]))

print(webs)

# many = 0
first = True
while True:
    # if (many < 1):
    #     sval = input("How many pages: ")
    #     if (len(sval) < 1):
    #         break
    #     many = int(sval)
    # many = many - 1
    if first == False:
        cur.execute("SELECT ID, URL FROM PAGES WHERE HTML IS NULL AND ERROR IS NULL AND (ID < 100 OR ID > 91271) ORDER BY RANDOM() LIMIT 1")
        try:
            row = cur.fetchone()
            print(row)
            fromid = row[0]
            url = row[1]
        except:
            print("No unretrieved pages found")
            many = 0
            break
    else:
        url = starturl

    cur.execute('SELECT ID FROM PAGES WHERE lower(URL) = ?', (url.lower(), ) )
    fromid = cur.fetchone()[0]
    print(fromid, url, end = " ")
    #If we are retrieving this page, there should be no links FROM it
    cur.execute("DELETE FROM LINKS WHERE FROM_ID = ?", (fromid, ) )
    try:
        document = urlopen(url, context = ctx)

        html = document.read()      #no need to decode into unicode because we are using BeautifulSoup
        if document.getcode() != 200:
            print("Error on page: ", document.getcode())
            cur.execute("UPDATE PAGES SET ERROR = ? WHERE lower(URL) = ?", (document.getcode(), url.lower()) )

        if "text/html" != document.info().get_content_type():
            print("Ignore non text/html page")
            cur.execute("DELETE FROM PAGES WHERE lower(URL) = ?", (url.lower(), ) )
            cur.execute("UPDATE PAGES SET ERROR = 0 WHERE lower(URL) = ?", (url.lower(), ) )
            conn.commit()
            continue

        print("(" + str(len(html)) +")", end = " ")

        soup = BeautifulSoup(html, "html.parser")
    except KeyboardInterrupt:
        print("")
        print("Program interrupder by user...")
        break
    except:
        print("Unable to retrieve or parse page")
        cur.execute("UPDATE PAGES SET ERROR = -1 WHERE lower(URL) = ?", (url.lower(), ) )
        conn.commit()
        continue

    cur.execute("INSERT OR IGNORE INTO PAGES (URL, HTML, NEW_RANK) VALUES (?, NULL, 1.0)", (url, ) )
    cur.execute("UPDATE PAGES SET HTML = ? WHERE lower(URL) = ?", (memoryview(html), url.lower()) )
    conn.commit()
    print("C")
    cur.execute("SELECT URL FROM WEBS")
    url = cur.fetchone()[0]

    #Retrieve all of the anchor tags
    tags = soup("a")
    #print(tags)
    count = 0
    for tag in tags:
        href = tag.get("href", None)
        # up = urlparse(href)
        # print("up = ", up)

        if href is None:
            # print("To Exclude", href)
            continue
        elif (
                (href.find("Main_Page") == -1) and
                (href.find("#") == -1) and
                (re.search('^http', href) is None) and
                ((not re.findall("^/wiki/", href)) is False) and
                (re.search("^/wiki/\S+:", href) is None)):
            # print("To crawle", href)
            up = urlparse(href)
        else:
            # print("Not Catched", href)
            continue
        href = urljoin(url, href)
        print("New href = ", href)

        #Check if the URL is in any of the web
        found = False
        for web in webs:
            if (href.startswith(web)):
                found = True
                break
        if not found:
            continue

        cur.execute("INSERT OR IGNORE INTO PAGES (URL, HTML, NEW_RANK) VALUES (?, NULL, 1.0)", (href , ) )
        count = count + 1
        conn.commit()

        cur.execute("SELECT ID FROM PAGES WHERE lower(URL) = ? LIMIT 1", (href.lower(), ) )
        try:
            row = cur.fetchone()
            toid = row[0]
        except:
            print("Could not retrieve id")
            continue
        print(fromid, toid)
        cur.execute("INSERT OR IGNORE INTO LINKS (FROM_ID, TO_ID) VALUES (?, ?)", (fromid, toid) )
        conn.commit()

    print(count)
    first = False

cur.close()
