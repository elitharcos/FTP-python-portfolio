import socket
import os

'''
Other Socket Types:
socket.
SOCK_STREAM: For TCP
SOCK_DGRAM: For UDP (User Datagram Protocol) connections, which are connectionless, faster, but less reliable than TCP.
SOCK_RAW: For raw sockets, which allow you to work with lower-level protocols like ICMP (used in ping) or to implement custom protocols.

Other Address Families:
socket.
AF_INET: ipv4 standard
AF_INET6: For IPv6 addresses.
AF_UNIX: For local communication within the same machine using Unix domain sockets.
'''

def fileSendOverTCP(_fileName="exampleFile.txt",_ipAddress="127.0.0.1",_port=12345,_receiverIP="127.0.0.1"):
    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverSocket.bind((_ipAddress,_port))
    serverSocket.listen(1)
    print("1")
    
    clientSocket, clientAddress = serverSocket.accept()
    print("2")

    print(clientAddress[0])

    if clientAddress[0] != _receiverIP:
        print(f"Unauthorized access attempt")
        clientSocket.close()
        serverSocket.close()
        return

    #rb means read binary
    with open(_fileName, "rb") as file:
        data = file.read()
        clientSocket.sendall(data)

        clientSocket.close()
        serverSocket.close()
        print("3")

def fileReceiverOverTCP(_fileName="exampleFileReceived.txt",_ipAddress="127.0.0.1",_port=12345):
    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientSocket.connect((_ipAddress,_port))

    #wb means write binary
    print("4")
    with open(_fileName, "wb") as file:
        print("5")
        data = clientSocket.recv(1024)
        while(data):
            file.write(data)
            data = clientSocket.recv(1024)
            print("6")
    clientSocket.close()

#fileReceiverOverTCP()
fileName = input("file name (with extension, example:\"example.txt\"): ")
targetIp = input("ip of the client: (example: 127.0.0.1): ")
targetPort = int(input("port of the client example: 12345: "))

fileSendOverTCP(fileName,"0.0.0.0",targetPort,targetIp)