fname = "romeo.txt"
fhand = open(fname)

#we want to treat "soft" as "soft!"
import string
print(string.punctuation)

print("\n\n")

counts = dict()
for line in fhand:
    line = line.rstrip()
    #line.translate(str.maketrans(fromstr, tostr, deletestr))
    line = line.translate(line.maketrans("", "", string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigword = None
bigcount = None
for word, count in counts.items():
    if bigcount == None or bigcount < count:
        bigword = word
        bigcount = count

print(bigword, bigcount)
