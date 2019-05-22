from socket import *

serverName = 'localhost'

serverPort = 12005

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

sentence = input('Send Traffic:')

clientSocket.send(str.encode(sentence))

reply = clientSocket.recv(1024)

print ('From Server: ', bytes.decode(reply))

sentence2 = input('Send Traffic:')

clientSocket.send(str.encode(sentence2))

reply2 = clientSocket.recv(1024)

print('From Server: ', bytes.decode(reply2))

sentence3 = input('Print list? "yes" or "no": ')
if(sentence3 == 'yes'):
	print('...')
	print('Client: ', sentence)
	print ('From Server: ', bytes.decode(reply))
	print('Client: ', sentence2)
	print('From Server: ', bytes.decode(reply2))
if(sentence3 == 'no'):
	clientSocket.close()
clientSocket.close()
