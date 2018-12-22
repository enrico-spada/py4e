import socket
import re

# URL = input("Enter - ")
URL = "http://www.dr-chuck.com/page2.htm"
host = re.findall("http://(.+)/", URL)[0]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect( (host, 80) )
except:
    print(f"{URL} does not exist.")
    quit()

cmd = f"GET {URL} HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

mysock.close()
print("Done")
