import socket


def sendData():
    data_b = bytes('发送内容。。。', encoding="GBK")

    udpSocKetSend = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udpSocKetSend.sendto(data_b, ('169.254.213.46', 6666))


# 接收
def receiveData():
    udpSocketRecaive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udpSocketRecaive.bind(("", 7788))

    recvData = udpSocketRecaive.recvfrom(1024 * 10)

    content, destInfo = recvData

    print("content is %s" % content)
    print("content is %s" % content.decode("gb2312"))


if __name__ == '__main__':
    sendData()
    receiveData()
