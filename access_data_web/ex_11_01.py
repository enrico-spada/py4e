import re

fname = "mbox.txt"
fhand = open(fname)

regex = input("Enter a regular expression: ")

count = 0
for line in fhand:
    result = re.search(regex, line)
    if result:
        count += 1

print(f"{fname} had {count} lines that matched {regex}")
