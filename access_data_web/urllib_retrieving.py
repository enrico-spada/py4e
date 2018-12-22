#urllib allows us to treat pages like files

import urllib.request

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand:
    print(line.decode())


#Note that we also receive the header
#but to print them we need to do it in a different way
