import http.client
import sys

def client(serverName, serverPort, path):
    connection = http.client.HTTPConnection(serverName, serverPort)
    connection.request("GET", path)
    response = connection.getresponse()
    print("Status: {} and reason: {}".format(response.status, response.reason))
    data = response.read()

    print(data.decode())

    connection.close()

if __name__ == "__main__":
    serverName = sys.argv[1]
    serverPort = sys.argv[2]
    path = sys.argv[3]

    client(serverName, serverPort, path)