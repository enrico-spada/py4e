fname = input("Enter file name:")
# fname = "mbox-short.txt"
try:
    fhand = open(fname)
except:
    print("File not exists.")
    quit()

count = dict()
for line in fhand:
    if not line.startswith("From "):
        continue
    line = line.split()
    person = line[1]
    count[person] = count.get(person, 0) + 1

tmp = sorted([(v, k) for k, v in count.items()], reverse = True)

for v, k in tmp[ : 1]:
    print(k, v)
# print([(k, v) for v, k in tmp[ : 1]])
