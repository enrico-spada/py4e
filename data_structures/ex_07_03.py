fname = input("Enter a file name: ")

if fname == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd")
    quit()

try:
    fhandle = open(fname, 'r')
except:
    print("File cannot be opened:", fname)
    quit()
    
count = 0
for line in fhandle:
    if line.startswith("Subject:"):
        count += 1
print("There were", count, "subject lines in", fname)
