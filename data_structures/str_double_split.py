fhand = open("mbox-short.txt")
for line in fhand:
    linen = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    email = words[1]
    host = email.split("@")
    print(host[1])
