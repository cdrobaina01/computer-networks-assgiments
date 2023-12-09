from socket import *
import ssl
import base64

# Encoding picture
with open("mail.jpg", "rb") as image:
    imageData = base64.b64encode(image.read())

# Adding picture to the message
msg = "\r\n I love computer networks!"
msg += image_data
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
# Las direcciones de correo y contraseña fueron modificadas después de probarlas
mailserver = smtp.gmail.com
mailPort = 587
mailUser = 'user@gmail.com'
mailPassword = '****'
mailFromAddress = 'from@gmail.com'
mailToAddress = 'to@gmail.com'

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, mailPort))

context = ssl.create_default_context()
clientSocketSSL = context.wrap_socket(clientSocket, server_hostname=mailserver)

recv = clientSocketSSL.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocketSSL.send(heloCommand.encode())
recv1 = clientSocketSSL.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Authentication
authCommand = 'AUTH LOGIN\r\n'
clientSocketSSL.send(authCommand.encode())
recvAuth = clientSocketSSL.recv(1024).decode()
print(recvAuth)
if recv1[:3] != '334':
    print('334 reply not received from server.')

# Username
clientSocketSSL.send(base64.b64encode(mailUser.encode()) + b'\r\n')
recvUsername = clientSocketSSL.recv(1024).decode()
print(recvUsername)
if recvUsername[:3] != '334':
    print('334 reply not received from server.')

# Password
clientSocketSSL.send(base64.b64encode(mailPassword.encode()) + b'\r\n')
recvPassword = clientSocketSSL.recv(1024).decode()
print(recvPassword)
if recvPassword[:3] != '235':
    print('235 reply not received from server. Authentication failed.')

# Send MAIL FROM command and print server response.
mailFromCommand = 'MAIL FROM: <'+ mailFromAddress + '>\r\n'
clientSocketSSL.send(mailFromCommand.encode())
recv2 = clientSocketSSL.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptCommand = 'RCPT TO: <'+ mailToAddress + '>\r\n'
clientSocketSSL.send(RTCommand.encode())
recv3 = clientSocketSSL.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocketSSL.send(dataCommand.encode())
recv4 = clientSocketSSL.recv(1024).decode()
print(recv4)
if recv4[:3] != '250':
    print('250 reply not received from server.')

# Send message data.
clientSocketSSL.send(msg.encode())

# Message ends with a single period.
clientSocketSSL.send(endmsg.encode())
recv5 = clientSocketSSL.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSocketSSL.send(quitCommand.encode())
recv5 = clientSocketSSL.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')

clientSocketSSL.close()