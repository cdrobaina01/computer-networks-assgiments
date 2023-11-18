from socket import *
import sys
import time

def client(serverName, serverPort):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    for i in range(10):
        time1 = time.time()
        outputdata = 'Ping ' + str(i) + " " + str(time1)
        clientSocket.settimeout(1)
        clientSocket.sendto(outputdata.encode(), (serverName, serverPort))
        try:
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            timeDiff = time.time() - time1
            print(modifiedMessage.decode() + " RTT: " + str(timeDiff))
        except:
            print("lost " + str(i))

if __name__ == "__main__":
    serverName = sys.argv[1]
    client(serverName, 12000)