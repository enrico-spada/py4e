import urllib.request

# URL = input("Enter - ")
URL = "http://data.pr4e.org/mbox-short.txt"

fhand = urllib.request.urlopen(URL)

count = 0
printed = 0
maximum = 3000
for line in fhand:
    count = count + len(line)
    text = line.decode()
    if ((printed + len(text)) > maximum) and printed < maximum:
        text = text[printed : maximum]
        print(text)
        printed = printed + len(text)
    elif printed < maximum:
        print(text)
        printed = printed + len(text)

print("done", printed, count)
quit()
