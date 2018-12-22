fhand = open("mbox-short.txt")

#we fine-tune the regex to avoid the string matched having whitespaces

import re
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if re.search("^X-\S+:", line):
        print(line)


#match lines starting with chars "X-"
#followed by NON whitespace characters (\S)
#one or more times (+)    --> * can be also 0 times
#followed by char ":"
