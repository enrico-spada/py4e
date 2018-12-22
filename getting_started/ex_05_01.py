total = 0
count = 0
average = None
while True :
    svalue = input("Enter a number: ")
    if value == "done":
        break
    else:
        try:
            ivalue = int(value)
        except:
            print("Invalid input")
            continue
    total = total + ivalue
    count = count + 1
print(total, count, total / count)
