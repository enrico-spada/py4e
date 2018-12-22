import urllib.request


#If the file is big, this code crashes!
img = urllib.request.urlopen("http://data.pr4e.org/cover3.jpg").read()
fhand = open("cover3.jpg", "wb")  #opens binary file for writing only
fhand.write(img)
fhand.close()


#Better to retrieve data in blocks (Buffers)
img = urllib.request.urlopen("http://data.pr4e.org/cover3.jpg")
fhand = open("cover3.jpg", "wb")
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1:
        break
    size = size + len(info)
    fhand.write(info)

print(size, "characters copied.")
fhand.close()

#with this mechanism we readed only 100000 chr at a time
#and then write them into cover3.jpg before retrieving the next 100000
