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

print( sorted( [(v, k) for k, v in words.items() ]) )
