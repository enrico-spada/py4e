fname = "mbox-short.txt"
fhand = open(fname)
count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    sender = words[1]
    count += 1
    print(sender)
print("There were", count, "lines in the file with From as the first word")
