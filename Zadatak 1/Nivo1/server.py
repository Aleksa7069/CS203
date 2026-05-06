import socket
import string

ip = 'localhost'
port = 33445

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((ip, port))
s.listen()

conn, addr = s.accept()

str = conn.recv(1024)

strhash = hash(str)
print(strhash)

if (strhash < 0):
    strhash = strhash * (-1)

conn.send(strhash.to_bytes(255, byteorder='big'))

conn.close()
s.close()
