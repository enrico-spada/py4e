import socket
import re

URL = "http://www.dr-chuck.com/page2.htm"
host = re.findall("http://(.+)/", URL)[0]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect( (host, 80) )
except:
    print(f"{URL} not exist.")
    quit()

cmd = f"GET {URL} HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

count = 0
tmp = 0
while True:
    data = mysock.recv(512)
    tmp = tmp + len(data)
    if tmp > 10:
        if (count - len(data)) <= 10:
            output_text =data.decode()[count : 10]
            print(output_text)
            count = count + len(output_text)
        break
    if len(data) < 1:
        break
    count = count + len(data)
    print(data.decode())


mysock.close()
print("Done", count)
