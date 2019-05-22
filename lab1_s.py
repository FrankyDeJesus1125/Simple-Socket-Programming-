from socket import *

serverPort = 12005

serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('localhost',serverPort))

serverSocket.listen(1)

print ('The server is ready')

connectionSocket, addr = serverSocket.accept()

while 1:

     sentence = connectionSocket.recv(1024)

     if(bytes.decode(sentence)=='Hello Fordham'):

     	print('From client: ', (sentence))

     	print('sending: Hello CIS Students')

     	connectionSocket.send(str.encode('Hello CIS Students'))

     elif(bytes.decode(sentence)=='Hello CISC4615'):

     	print('From Client: ', sentence)

     	print('sending: Bye!')

     	connectionSocket.send(str.encode('Bye!'))

     	break

connectionSocket.close()


