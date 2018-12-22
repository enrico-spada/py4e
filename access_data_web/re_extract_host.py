import re

fhand = open("mbox-short.txt")

hostlist = list()
for line in fhand:
    host = re.findall("^From .+@([^ ]+)", line)   #\S+ is the same of [^ ]+ and .+
    if host:
        hostlist.extend(host)

print(hostlist)
