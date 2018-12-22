# fhand = open("mbox-short.txt")
# for line in fhand:
#     if line.startswith("From"):
#         print(line)


#note that print() adds a new line!
#let's try to remove it
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From: "):
        print(line)


#Another way to accomplish the same task
# fhand = open("mbox-short.txt")
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith("From: "):
#         continue
#     print(line)
