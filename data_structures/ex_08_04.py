fname = "romeo.txt"
fhand = open(fname)
text = list()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in text:
            text.append(word)
text.sort()
print(text)     
