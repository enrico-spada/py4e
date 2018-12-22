fruit = "banana"

#Indetermined loop
index = 0
while index < len(fruit) :
    letter = fruit[index]
    print(index, letter)
    index += 1

print("\n\n")

#Determined loop
for letter in fruit :
    print(letter)

#It always better to use a more succint and simpler piece of code to accomplish what you want
#easier to read, easier to code, and easier to debug
