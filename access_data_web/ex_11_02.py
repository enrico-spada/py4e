import re

fname = "mbox.txt"
fhand = open(fname)

values = list()
for line in fhand:
    value = re.findall("^New Revision: ([0-9]+)", line)
    if value:
        print(value)
        print(line)
        values.extend(value)

values = list(map(int, values))
print(sum(values) / len(values))
