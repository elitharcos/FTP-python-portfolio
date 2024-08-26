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

def fileSendOverTCP(_fileName="exampleFile.txt",_ipAddress="127.0.0.1",_port=12345):
    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverSocket.bind((_ipAddress,_port))
    serverSocket.listen(1)
    print("1")

    clientSocket, clientAddress = serverSocket.accept()
    print("2")
    #rb means read binary
    with open(_fileName, "rb") as file:
        data = file.read()
        clientSocket.sendall(data)

        clientSocket.close()
        serverSocket.close()
        print("3")

def fileReceiverOverTCP(_fileName="exampleFileReceived.txt",_ipAddress="127.0.0.1",_port=12345): #port here refers to the sender's port
    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        clientSocket.connect((_ipAddress,_port))
    except Exception as error:
        print(error)

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

fileName=input("say file to create name with extension: ")
ipAddress = input("say the ipv4 of the sender: ")
port = int(input("say your port: "))
fileReceiverOverTCP(fileName,ipAddress,port)
#fileSendOverTCP()