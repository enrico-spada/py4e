fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("File does not exist.")

domain_list = list()
counts = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    line = line.split()
    email = line[1]
    domain = email.split("@")[1]
    counts[domain] = counts.get(domain, 0) + 1
    domain_list.append(domain)

print(counts)
