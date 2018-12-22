counts = dict()
names = ["csven", "cwen", "csev", "zqian", "cwen"]
for name in names:
    counts[name] = counts.get(name, 0) + 1  #if the name is not present assign 0. Next, add 1
print(counts)
