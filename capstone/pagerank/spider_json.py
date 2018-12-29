import sqlite3

conn = sqlite3.connect("db_spider.sqlite")
cur = conn.cursor()

print("Creating JSON output on spider.js")
howmany = int(input("How many nodes?"))

cur.execute('''
            SELECT  COUNT(FROM_ID) AS INBOUND,
                    OLD_RANK,
                    NEW_RANK,
                    ID,
                    URL
            FROM    PAGES
            JOIN    LINKS
                ON  PAGES.ID = LINKS.TO_ID
            WHERE   HTML IS NOT NULL
                    AND ERROR IS NOT NULL
            GROUP BY ID
            ORDER BY ID, INBOUND
            ''')

fhand = open("spider.js", "w")
nodes = list()
maxrank = None
minrank = None
for row in cur:
    nodes.append(row)
    rank = row[2]
    if maxrank is None or maxrank < rank:
        maxrank = rank
    if minrank is None or minrank > rank:
        minrank = rank
    if len(nodes) > howmany:
        break

if maxrank == minrank or marank is None or minrank is None:
    print("Error - please run sprank.py to compute pagerank")
    quit()

fhand.write('spiderJson = {"nodes":[\n')
count = 0
map = dict()
ranks = dict()
for row in nodes:
    if count > 0:
        fhand.write(", \n")
        #print(row)
        rank = row[2]
        rank = 19 * ( (rank - minrank) / (maxrank - minrank) )   #normalize the rank so it becomes the thickness of the line
        fhand.write('{' + '"weight":' + str(row[0]) + ', "rank": ' + str(rank) + ',')
        fhand.write(' "id":' + str(row[3]) + ', "url":"' + row[4] + '"}')
        map[row[3]] = count
fhand.write("],\n")

cur.execute("SELECT DISTINCT FROM_ID, TO_ID FROM LINKS")
fhand.write('"links":[\n')

count = 0
for row in cur:
    #print(row)
    if row[0] not in map or row[1] not in map:
        continue
    if count > 0:
        fhand.write(",\n")
        rank = ranks[row[0]]
        srank = 19 * (rank - minrank) / (maxrank - minrank)
        fhand.write('{"source":'+str(map[row[0]])+',"target":'+str(map[row[1]])+',"value":3}')
        count = count + 1
fhand.write(']};')
fhand.close()
cur.close()

print("Open force.html in a browser to view the visualization ")
