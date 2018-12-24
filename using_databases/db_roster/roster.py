import json
import sqlite3

conn = sqlite3.connect("rosterdb.sqlite")       #make a DB connection
cur = conn.cursor()                             #get a cursor; like the fhandle to the db server

cur.executescript('''
DROP TABLE IF EXISTS USER;
DROP TABLE IF EXISTS MEMBER;
DROP TABLE IF EXISTS COURSE;

CREATE TABLE USER(
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    NAME TEXT UNIQUE
);

CREATE TABLE COURSE(
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    TITLE TEXT UNIQUE
);

CREATE TABLE MEMBER(
    USER_ID INTEGER,
    COURSE_ID INTEGER,
    ROLE INTEGER,
    PRIMARY KEY (USER_ID, COURSE_ID)
);
''')

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "roster_data_sample.json"

#Sample json
# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)            #results in an array of arrays

for entry in json_data:

    name = entry[0]
    title = entry[1]
    role = entry[2]

    print( (name, title, role) )

    cur.execute('''
                INSERT OR IGNORE INTO USER (NAME)
                VALUES
                (?)''',
                (name, )
                )
    cur.execute('SELECT ID FROM USER WHERE NAME = ?', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''
                INSERT OR IGNORE INTO COURSE (TITLE)
                VALUES
                (?)''',
                (title, )
                )
    cur.execute('SELECT ID FROM COURSE WHERE TITLE = ?', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''
                INSERT OR REPLACE INTO MEMBER (USER_ID, COURSE_ID, ROLE)
                VALUES
                (?, ?, ?)''',
                (user_id, course_id, role)
                )

    conn.commit()
