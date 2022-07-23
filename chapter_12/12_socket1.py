import socket
# socket still not connected; here some kind of file handler
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()    
# .encode() -> prepare the data to go across the internet
# -> takes a unicode string and turns it into a UTF-8 bites to transport it
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end = '')
    # .decode() -> takes a UTF-8 bite and turns it into a unicode string 
mysock.close()