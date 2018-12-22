values = list()
while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        ival = int(sval)
    except:
        print("Please enter a number")
        continue
    values.append(ival)

print("Maximum:", max(values))
print("Minimum:", min(values))
