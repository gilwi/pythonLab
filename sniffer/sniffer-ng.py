#!/usr/bin/python3

import socket
from ethdata import EthData
from ipdata import IpData

def main():
    s = socket.socket(
        socket.AF_PACKET,
        socket.SOCK_RAW,
        socket.htons(3)
    )
    frameCount=0

    s.bind(('eth1', 3))

    while True:
        message = s.recv(1024)

        eth_layer = EthData(message)
        print()
        print("This is packet number :", frameCount)
        print(eth_layer.mac_dst)
        print(eth_layer.mac_src)
        print(eth_layer.eth_type)
        print()

        if eth_layer.eth_type == '0800':
            ip_layer = IpData(message[14:-4])

            print(ip_layer.ip_header[16:20])


        frameCount+=1

if __name__ == '__main__':
    main()
