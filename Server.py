from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('server is up and ready')
while True:
    connectionSocket, clientAddr = serverSocket.accept()
    print('connection established with {}'.format(clientAddr))
    message = serverSocket.recv(2048).decode()
    print('{}: {}'.format(clientAddr, message))
    modifiedMessage = message.upper()
    print('sending server response ({}) to {}'.format(modifiedMessage, clientAddr))
    serverSocket.send(modifiedMessage.encode())
    print('response sent.')
    connectionSocket.close()
