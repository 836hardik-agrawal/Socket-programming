import socket

s = socket.socket()
print('socket created')
s.bind(('192.168.43.110', 9999))

s.listen(3)
print('waiting for connections')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("connected with", addr, name)

    c.send(bytes('welcome to server'+" "+name, 'utf-8'))
s.close()
