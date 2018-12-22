fname = input("Enter file name: ")
# fname = "mbox-short.txt"
try:
    fhand = open(fname)
except:
    print("File not exists.")
    quit()

import string

text = fhand.read()

print(string.punctuation)
text = text.translate( text.maketrans( "", "", string.punctuation + " " + "\n" + "\t"))
text = text.lower()
counter = dict()
for j in range(len(text)):
    letter = text[j]
    if not letter.isalpha():
        continue
    counter[letter] = counter.get(letter, 0) + 1

tmp = sorted( [ (count, letter) for letter, count in counter.items() ], reverse = True )
print(tmp)

for count, letter in tmp:
    print(letter)
