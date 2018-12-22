fhand = open("mbox-short.txt")

import re
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if re.search("^X.*:", line):
        print(line)
