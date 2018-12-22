fname = input("Enter a file name:")
try:
    fhand = open(fname)
except:
    print("File name does not exist.")
    quit()

email_list = list()
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    line = line.split()
    email_list.append(line[1])

counts = dict()
for email in email_list:
    counts[email] = counts.get(email, 0) + 1

bigemail = None
bigcount = None
for email, count in counts.items():
    if bigcount == None or bigcount < count:
        bigemail = email
        bigcount = count

print(bigemail, bigcount)
