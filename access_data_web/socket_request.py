import socket

#creates the doorway but there is nothing connect to it
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#create the connection
mysock.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
                                            #take this string and tranform it from UNICODE to UTF-8 (default)
    #.encode() is like "prepare for sending"
    #\r\n\r\n is because in TELNET you used to do ENTER ENTER
mysock.send(cmd)

while True:
    data = mysock.recv(512)    #we receive up to 512 characters
        #note the string received is of type 'bytes'
    if (len(data) < 1):       #if we get no data it means end of file / end of transmission
        break
    print(data.decode())      #if we did get data, we decode it from UTF-8 (default) to UNICODE
        #now data are string type 'str'
mysock.close()
