import re

fhand = open("mbox-short.txt")
numlist = list()
for line in fhand:
    spam = re.findall("^X-DSPAM[^ ]+: ([0-9.]+)", line)
    #this look for the line containing SPAM confidence and extract the numeric score
    if spam:
        numlist.extend(spam)

print("Maximum: ", max(numlist))
