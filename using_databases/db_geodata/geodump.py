import sqlite3
import json
import codecs

conn = sqlite3.connect("geodata.sqlite")
cur = conn.cursor()

cur.execute("SELECT * FROM LOCATIONS")
fhand = codecs.open("where.js", "w", "utf-8")
fhand.write("myData = [\n")
count = 0
for row in cur:
    data = str(row[1])
    try:
        js = json.loads(str(data))[0]
    except:
        continue

    if not(int(js["place_id"]) > 0):
        continue

    lat = float(js["lat"])
    lng = float(js["lon"])
    if lat == 0 or lng == 0:
        continue
    where = js["display_name"]
    where = where.replace("'", "")
    try:
        print(where, lat, lng)

        if (count + 1) > 1:
            fhand.write(",\n")
        output = "[" + str(lat) + ", " + str(lng) + ", '" + where + "']"
        fhand.write(output)
        count = count + 1
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")
