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

    s.bind(('eth0', 3))

    while True:
        message = s.recv(1024)

        eth_layer = EthData(message)
        print()
        print("This is packet number :", frameCount)
        print(eth_layer.mac_dst)
        print(eth_layer.mac_src)
        print(eth_layer.eth_type)
        print()

        ip_layer = IpData(message)
        # print(ip_layer.version)
        # print(ip_layer.hdr_len)
        # print(ip_layer.tos)
        # print(ip_layer.ecn)
        # print(ip_layer.pkt_len)
        # print(ip_layer.frag_id)
        # print(ip_layer.flags)
        # print(ip_layer.frag_offset)
        # print(ip_layer.ttl)
        # print(ip_layer.proto)
        # print(ip_layer.hdr_cksum)
        print(ip_layer.src_addr)
        print(ip_layer.dst_addr)


        frameCount+=1

if __name__ == '__main__':
    main()

    self.version = self.ip_header[0:3]
    self.hdr_len = self.ip_header[4:8]
    self.tos = self.ip_header[8:14]
    self.ecn = self.ip_header[14:16]
    self.pkt_len = self.ip_header[16:32]
    self.frag_id = self.ip_header[32:48]
    self.flags = self.ip_header[48:51]
    self.frag_offset = self.ip_header[51:64]
    self.ttl = self.ip_header[64:72]
    self.proto = self.ip_header[72:80]
    self.hdr_cksum = self.ip_header[80:96]
    self.src_addr = self.ip_header[96:128]
    self.dst_addr = self.ip_header[128:160]