import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect( ("data.pr4e.org", 80) )

cmd = "GET http://data.pr4e.org/romeo.txt HTTPS/1.0\r\n\r\n".encode()

mysock.send(cmd)

doc = str()
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    doc += data.decode()


pos = doc.find("\r\n\r\n")   #this allows us to find the FIRST new line, meaning the Header is finished
print(doc[pos + 4 : ])
