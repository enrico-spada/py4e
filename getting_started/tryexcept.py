astr = "Hello Bob"
try:
    istr = int(astr)
except:   #python executes this code if something goes wrong
    istr = -1

print("First", istr)


astr = "123"
try:
    istr = int(astr)
except:   #python executes this code if something goes wrong
    istr = -1

print("Second", istr)
