import socket


# TDP服务端
def receiveData():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(("", 8899))
    serverSocket.listen(5)

    clientSocket, clientInfo = serverSocket.accept()

    recvData = clientSocket.recv(1024)
    print("TDP服务端")
    print(clientInfo)
    print(recvData)

    clientSocket.close()
    serverSocket.close()


# TDP客户端
def sendData():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(("127.0.0.1", 6666))

    clientSocket.send(b"zhang")

    recvData = clientSocket.recv(1024)
    print("TDP客户端")
    print(recvData)


if __name__ == '__main__':
    # receiveData()
    sendData()
