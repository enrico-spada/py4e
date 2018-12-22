fhand = open("mbox-short.txt")

# for line in fhand:
#     line = line.rstrip()
#     if line.find("From:") >= 0:  #find returns the position or -1 if not found !
#         print(line)
#

import re
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if re.search("From", line):
        print(line)
