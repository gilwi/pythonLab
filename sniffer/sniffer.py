import socket
from ethdata import EthData

def main():
    s = socket.socket(
        socket.AF_PACKET,
        socket.SOCK_RAW,
        socket.htons(3)
    )

    s.bind(('eth0', 3))

    while True:
        message = s.recv(1024)
        frame = EthData(message)
        print(frame.bytes)
        print(frame.mac_dst)
        print(frame.mac_src)
        print(frame.eth_type)



if __name__ == '__main__':
    main()

