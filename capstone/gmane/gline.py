import sqlite3
import time
import zlib

conn = sqlite3.connect("index.sqlite")
cur = conn.cursor()

cur.execute("""
            SELECT  ID, SENDER
            FROM    SENDERS
            """)
senders = dict()
# Pre-load all the senders
for message_row in cur:
    senders[message_row[0]] = message_row[1]


cur.execute("""
            SELECT  ID, GUID, SENDER_ID,
                    SUBJECT_ID, SENT_AT
            FROM    MESSAGES
            """)
messages = dict()
# Pre-load all the messages
for message_row in cur:
    messages[message_row[0]] = (message_row[1], message_row[2], message_row[3], message_row[4])

print("Loaded messages=", len(messages), "senders=", len(senders))

sendorgs = dict()
# Read through all messages
for (message_id, message) in list(messages.items()):
    sender = message[1]
    pieces = senders[sender].split("@")
    if len(pieces) != 2:
        continue
    dns = pieces[1]
    sendorgs[dns] = sendorgs.get(dns, 0) + 1

# Pick the top schools
orgs = sorted(sendorgs, key = sendorgs.get, reverse = True)
orgs = orgs[ : 10]
print("Top 10 organizations")
print(orgs)

counts = dict()
months = list()
#Break the top schools into months
for (message_id, message) in list(messages.items()):
    sender = message[1]
    pieces = senders[sender].split("@")
    if len(pieces) != 2:
        continue
    dns = pieces[1]
    if dns not in orgs:
        continue
    month = message[3][ : 7]
    if month not in months:
        months.append(month)
    key = (month, dns)      #we create a dictionary where the key is a tuple
    counts[key] = counts.get(key, 0) + 1

months.sort()
print (counts)
print (months)

fhand = open("gline.js", "w")
fhand.write("gline = [ [ 'Month'")
for org in orgs:
    fhand.write(",'" + org + "'")
fhand.write("]")

for month in months:
    fhand.write(",\n['" + month + "'")
    for org in orgs:
        key = (month, org)
        val = counts.get(key, 0)
        fhand.write("," + str(val))
    fhand.write("]")

fhand.write("\n];\n")
fhand.close()

print("Output written in gline.js")
print("Open gline.htm to visualize the data")
