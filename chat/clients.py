import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('localhost',1111))

flag=True

while flag:
    client.send(input('Я:').encode('utf-8'))
    msg=client.recv(1024).decode('utf-8')
    if msg=='quit':
        flag=False
    else:
        print(msg)

client.send(input('Server: ').encode('utf-8'))

client.close()

