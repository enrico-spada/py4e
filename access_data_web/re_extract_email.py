import re

fhand = open("mbox-short.txt")

for line in fhand:
    email = re.findall("^From (\S+@\S+)", line)   #start extracting after the space!
    if email:
        print(email)


# for line in fhand:
#     email = re.findall("\s<.(\S+@\S+[.][a-z]+)", line)
#     if email:
#         print(email)
#

# for line in fhand:
#     email = re.findall("\S@\S+", line)
#     if not email:
#         continue
#     print(email)
