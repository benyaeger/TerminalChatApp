from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('server is up and ready')
connectionSocket, clientAddr = serverSocket.accept()
print('connection established with {}'.format(clientAddr))
while True:
    message = connectionSocket.recv(2048).decode()
    print('{}: {}'.format(clientAddr, message))
    response = input('enter:')
    connectionSocket.send(response.encode())