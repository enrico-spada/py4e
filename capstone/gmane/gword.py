import sqlite3
import time
import zlib
import string

conn = sqlite3.connect("index.sqlite")
cur = conn.cursor()

cur.execute("""
            SELECT  ID, SUBJECT
            FROM    SUBJECTS
            """)
subjects = dict()
for message_row in cur:
    subjects[message_row[0]] = message_row[1]

cur.execute("""
            SELECT  SUBJECT_ID
            FROM    MESSAGES
            """)
counts = dict()
for message_row in cur:
    text = subjects[message_row[0]]     #use SUBJECT_ID to lookup SUBJECT from SUBJECTS table
    text = text.translate(str.maketrans("", "", string.punctuation))
#str.translate(table[, deletechars])
        #returns a copy of the string in which all characters have been translated
        #using table (constructed with maketrans() function of string module)
#str.maketrans(intab[, outtab[, z])
        #returns a translation table that maps each character in the intab
        #into the character at the same position of the outtab string
        #if there is only one argument, it must be a dictionary
        #if there are two arguments, they must be string of equal length: len(intab) == len(outtab)
        #if there is a third argument, it must be a string, whose characters will be remove from the string
    text = text.translate(str.maketrans("", "", "1234567890"))
    text = text.strip().lower()
    words = text.split()
    for word in words:
        if len(words) < 4:
            continue
        counts[word] = counts.get(word, 0) + 1

x = sorted(counts, key = counts.get, reverse = True)
highest = None
lowest = None
for k in x[ : 100]:
    if highest is None or highest < counts[k]:
        highest = counts[k]
    if lowest is None or lowest > counts[k]:
        lowest = counts[k]
print("Range of counts:", highest, lowest)

# Spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20

#Produce the file to feed the .js visualizer
fhand = open("gword.js", "w")
fhand.write('gword = [  ')
first = True
for k in x[ : 100]:
    if not first:
        fhand.write(",\n")
    first = False
    size = counts[k]
    size = (size - lowest) / float(highest - lowest)
    size = int((size * bigsize) + smallsize)
    fhand.write("{text: '" + k + "', size: " + str(size) + "}")
fhand.write("\n];\n")
fhand.close()

print("Output written to gword.js")
print("Open gword.htm in a browser to see the visualization")
