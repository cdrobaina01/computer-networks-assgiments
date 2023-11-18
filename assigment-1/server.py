from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 80
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        outputdata = 'HTTP/1.1 200 OK\r\n\r\n' + outputdata
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
        print("OK!")
    except IOError:
        outputdata = 'HTTP/1.1 404 Not Found\r\n\r\n'
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()

serverSocket.close()
sys.exit()