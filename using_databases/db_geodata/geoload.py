import urllib.request, urllib.error, urllib.parse
import http
import json
import sqlite3
import time
import ssl
import sys
import random

# Ignore SSL Certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

service_url = "https://nominatim.openstreetmap.org/search?"

conn = sqlite3.connect("geodata.sqlite")
cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS LOCATIONS
            (ADDRESS TEXT,
            GEODATA TEXT,
            RUN_FL INTEGER)
            ''')

fname = "where.data"
fhandle = open(fname)
count = 0
for line in fhandle:
    if count > 200:
        print("Retrieved 200 locations, restart to retrieve more")
        break

    address = line.strip()
    print("")
    cur.execute("SELECT GEODATA FROM LOCATIONS WHERE ADDRESS = ?",
                (address, ) )

    try:
        data = cur.fetchone()[0]
        print("Found in database ", address)
        continue
    except:
        pass

    time.sleep(random.uniform(1,1.3))
    parms = dict()
    parms["q"] = address
    parms["format"] = "json"
    parms["limit"] = 1
    parms["amenity"] = "university"
    parms["type"] = "university"
    url = service_url + urllib.parse.urlencode(parms)

    print("Retrieving", url)
    uh = urllib.request.urlopen(url, context = ctx)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters", data[ : 20].replace("\n", " "))
    count = count + 1

    try:
        js = json.loads(data)[0]
    except:
        print(data)
        cur.execute('''
            INSERT INTO LOCATIONS (ADDRESS, GEODATA, RUN_FL)
            VALUES
            (?, ?, 1)''',
            (address, data))
        conn.commit()
        continue

#    print(json.dumps(js, indent = 2))

    try:
        int(js["place_id"]) > 0
    except:
        print('==== Failure To Retrieve ====')
        print(data)
        cur.execute('''
                INSERT INTO LOCATIONS (ADDRESS, GEODATA, RUN_FL)
                VALUES
                (?, ?, 1)''',
                (address, data))
        conn.commit()
        break

    cur.execute('''
                INSERT INTO LOCATIONS (ADDRESS, GEODATA, RUN_FL)
                VALUES
                (?, ?, 1)''',
                (address, data))

    conn.commit()
    if count % 10 == 0:
        print("Pausing for a bit...")
        time.sleep(random.uniform(4.5,5.5))


print("Run geodump.py to read the data from the database so you can vizualize it on a map.")


# data = '[{"place_id":"198561071","licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":"1839026","boundingbox":["53.4598667","53.4716848","-2.2390346","-2.2262754"],"lat":"53.46600455","lon":"-2.23300880782987","display_name":"University of Manchester - Main Campus, Brunswick Street, Curry Mile, Ardwick, Manchester, Greater Manchester, North West England, England, M13 9NR, United Kingdom","class":"amenity","type":"university","importance":0.31100000000000005,"icon":"https://nominatim.openstreetmap.org/images/mapicons/education_university.p.20.png"}]'
# print(data)
# js = json.loads(data)[0]
# print(js["place_id"])
# print(type(js))
# print(json.dumps(js, indent = 2))
