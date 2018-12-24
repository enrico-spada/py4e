import sqlite3          #SQLite is so light it is built-in inside Python
import re

conn = sqlite3.connect("emaildb.db")
    #if the file does not exists, it is created
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts
''')

cur.execute('''
CREATE TABLE COUNTS (EMAIL TEXT, COUNT INTEGER)
''')

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fhandle = open(fname)

for line in fhandle:
    if not line.startswith("From: "):
        continue
    # email = re.findall("\S+@\S+", line)
    line = line.split()
    email = line[1]
#the next statements are like the dictionary.get() operation
     #this syntax is not really retrieving the data, we only prepared the cursos
    cur.execute('''
    SELECT COUNT FROM COUNTS WHERE EMAIL = ?
    ''',
    #? is a placeholder to avoid SQL Injection
    (email, )  #each position in the tuple substitute one ?. we need to put the comma otherwise it is not turn into a tuple ;)
    )

    row = cur.fetchone()                #grab the first record and give it back
    if row is None:
        cur.execute('''
                    INSERT INTO COUNTS (EMAIL, COUNT)
                    VALUES
                    (?, 1)
                    ''',
                    (email, )
                    )
    else:
        cur.execute('''
                    UPDATE COUNTS SET COUNT = COUNT + 1 WHERE EMAIL = ?
                    ''',
                    (email, )
                    )

    conn.commit()

sqlstr = 'SELECT EMAIL, COUNT FROM COUNTS ORDER BY COUNT DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])


cur.close()
