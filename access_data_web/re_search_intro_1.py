fhand = open("mbox-short.txt")

# for line in fhand:
#     line = line.rstrip()
#     if line.startswith("From:"):
#         print(line)
#

import re
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if re.search("^From", line):   #I want 'F' to be the first char of the line
        print(line)
