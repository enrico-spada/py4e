data = "From stephen.marquard@uct.ac.za Sat Jan  5  09:14:16 2008"
#we want to extract the host
atpos = data.find("@")
print(atpos, data[atpos])
sppos = data.find(" ", atpos)
print(sppos, data[sppos])
host = data[atpos+1 : sppos]
print(host)
