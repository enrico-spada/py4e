import sqlite3
import time
import zlib

howmany = int(input("How many to dump? "))

conn = sqlite3.connect("index.sqlite")
cur = conn.cursor()

cur.execute("SELECT ID, SENDER FROM  SENDERS")
senders = dict()
for message_row in cur:
    senders[message_row[0]] = message_row[1]

cur.execute("SELECT ID, SUBJECT FROM SUBJECTS")
subjects = dict()
for message_row in cur:
    subjects[message_row[0]] = message_row[1]

cur.execute("""
            SELECT  ID, GUID, SENDER_ID, SUBJECT_ID, SENT_AT
            FROM    MESSAGES
            """)

messages = dict()       #cache the data so it is faster
for message_row in cur:
    messages[message_row[0]] = (message_row[1], message_row[2], message_row[3], message_row[4])

print("Loaded messages =", len(messages), "subjects=", len(subjects), "senders=", len(senders))

sendcount = dict()      #cache the data so it is faster
sendorgs = dict()       #cache the data so it is faster
for (message_id, message) in list(messages.items()):
    sender = message[1]         #get the person
    sendcount[sender] = sendcount.get(sender, 0) + 1
    pieces = senders[sender].split("@")     #break the sender into pieces
    if len(pieces) != 2:                    #if there are not 2 pieces, continue
        continue
    dns = pieces[1]             #get the domain name
    sendorgs[dns] = sendorgs.get(dns, 0) + 1

print("")
print("Top", howmany, "Email list partecipants")

x = sorted(sendcount, key = sendcount.get, reverse = True)
for k in x[ : howmany]:
    print(senders[k], sendcount[k])
    if sendcount[k] < 10:
        break

print("")
print("Top", howmany, "Email list organizations")
x = sorted(sendorgs, key = sendorgs.get, reverse = True)        #sort by value (sendorgs.get("umich.edu")), reversed
for k in x[ : howmany]:
    print(k, sendorgs[k])
    if sendorgs[k] < 10:        #print out only the top 10
        break
