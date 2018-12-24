import xml.etree.ElementTree as ET   # we need this to deal with XML file generated from itunes
import sqlite3

conn = sqlite3.connect("trackdb.sqlite")

cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS ARTIST;
DROP TABLE IF EXISTS ALBUM;
DROP TABLE IF EXISTS TRACK;

CREATE TABLE ARTIST (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    NAME TEXT UNIQUE
);

CREATE TABLE ALBUM (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    ARTIST_ID INTEGER,
    TITLE TEXT UNIQUE
);

CREATE TABLE TRACK (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    TITLE TEXT UNIQUE,
    ALBUM_ID INTEGER,
    ARTIST_ID INTEGER,
    LEN INTEGER,
    RATING INTEGER,
    COUNT INTEGER
);
''')


fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "Library.xml"

#XML Format sample:
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):     #we need this function because the key of an object is inside the object itself
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == "key" and child.text == key:
            found = True
    return None

#First thing we do is parse the XML file
stuff = ET.parse(fname)
all_tracks = stuff.findall("dict/dict/dict")       #we go to the third level dictionaries to see all the tracks
print('Dict count:', len(all_tracks))
for entry in all_tracks:
    if (lookup(entry, 'Track ID') is None):     #if there is no track ID, we continue
        continue

    name = lookup(entry, "Name")
    artist = lookup(entry, "Artist")
    album = lookup(entry, "Album")
    count = lookup(entry, "Play Count")
    rating = lookup(entry, "Rating")
    length = lookup(entry, "Total Time")

    #Let's do some sanity checking
    if name is None or artist is None or album is None:
        continue

    print(name, "|", artist, "|", album, "|", count, "|", rating, "|", length)

    #INSERT OR IGNORE: if the value (UNIQUE NAME, NB: Create Table script), don't insert anything
    cur.execute('''
                INSERT OR IGNORE INTO ARTIST (NAME)
                VALUES
                (?)
                ''',
                (artist, )
                )

    cur.execute('SELECT ID FROM ARTIST WHERE NAME = ?',
                (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''
                INSERT OR IGNORE INTO ALBUM (ARTIST_ID, TITLE)
                VALUES
                (?, ?)
                ''',
                (artist_id, album)
                )

    cur.execute('SELECT ID FROM ALBUM WHERE TITLE = ?',
                (album, ))
    album_id = cur.fetchone()[0]

    #INSERT OR REPLACE: INSERT OR UPDATE
    cur.execute('''
                INSERT OR REPLACE INTO TRACK (TITLE, ALBUM_ID, LEN, RATING, COUNT)
                VALUES
                (?, ?, ?, ?, ?)
                ''',
                (name, album_id, length, rating, count)
                )

    conn.commit()

cur.close()
