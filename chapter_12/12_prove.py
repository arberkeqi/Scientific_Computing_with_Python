import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# (goes across the int, series of char come one after another)
mysock.connect(("data.pr4e.org", 80))   # ("Host", Port)

# http://www.dr-chuck.com/page1.html
# protocol      host        document
