# while True:
#     line = input('> ')
#     if line[0] == "#":
#         continue
#     if line == "done":
#         break
#     print(line)
# print("Done!")

#If the user enters ""
#IndexError: string index out of range

#Safely write the if statement using the guardian pattern
while True:
    line = input('> ')
    if len(line) > 0 and line.startswith("#"):
        continue
    if line == "done":
        break
    print(line)
print("Done!")
