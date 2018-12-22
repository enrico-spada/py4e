fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File name not exists.")
    quit()

counts = dict()
for line in fhand:
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
