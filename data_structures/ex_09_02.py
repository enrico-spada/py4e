fname = input("Enter a file name: ")
# fname = "mbox-short.txt"
try:
    fhand = open(fname)
except:
    print("The file does not exist.")
    quit()

days = list()
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    days.append(words[2])

counts = dict()
for day in days:
    counts[day] = counts.get(day, 0) + 1

print(counts)
