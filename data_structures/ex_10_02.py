# fname = input("Enter file name: ")
fname = "mbox-short.txt"
try:
    fhand = open(fname)
except:
    print("File not exists")
    quit()

counter = dict()
for line in fhand:
    if not line.startswith("From "):
        continue
    line = line.split()
    time = line[5]
    hour = time.split(":")[0]
    counter[hour] = counter.get(hour, 0) + 1

# print( sorted( [ (h, c) for h, c in counter.items() ] ) )
counter = sorted( [ (h, c) for h, c in counter.items() ] )
for h, c in counter:
    print(h, c)
