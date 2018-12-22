fname = input("Enter a file name:")
try:
    fhand = open(fname)
except:
    print("File does not exist")
    quit()

words = dict()
for line in  fhand:
    line = line.split()
    for word in line:
        words[word] = words.get(word, 0) + 1

tmp = list()
for k, v in words.items():
    newtup = (v, k)
    tmp.append(newtup)


#tmp.sort(reverse = True)
tmp = sorted(tmp, reverse = True)
for v, k in tmp[ : 10]:
    print(k, v)
