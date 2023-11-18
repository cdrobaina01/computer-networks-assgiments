#import socket module
from socket import *
import threading

def webProcess(connectionSocket):
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:], "rb")
        outputdata = f.read()
        outputdata = outputdata.decode()
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

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 80
serverSocket.bind(("", serverPort))
serverSocket.listen(10)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    thread = threading.Thread(target = webProcess, args = (connectionSocket, ))
    thread.start()
serverSocket.close()