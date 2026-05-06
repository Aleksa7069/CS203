import socket

ip = 'localhost'
port = 33445

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

string = input("Unesi poruku: ")

if (len(string) > 255):
    print("Uneli ste string vise od 255 karaktera")
else:
    print("String pre hesiranja: " + string)
    s.send(string.encode())
    strhes = s.recv(1024)
    print("Posle hesiranja: ")
    print(strhes)

