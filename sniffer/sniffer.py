#!/usr/bin/python3

import socket
from struct import unpack

class L2Data:

    def __init__(self, bytes):

        # Retrieve ethernet encapsulation data
        self.__eth_header = bytes
        # self.eth_fcs = self.bytes[-4:]

        # Retrieve formatted string corresponding to
        # ethernet header information
        self.dst_mac = fmt_macaddr(self.__eth_header[:6].hex())
        self.src_mac = fmt_macaddr(self.__eth_header[6:-2].hex())
        self.eth_type = self.__eth_header[-2:].hex()

    def __repr__(self):
        return "DST_MAC: {}\nSRC_MAC: {}\nETH_TYPE: {}".format(self.dst_mac,
                                                               self.src_mac,
                                                               self.eth_type)

class IPData:

    def __init__(self, bytes):

        # Retrieve ethernet encapsulation data
        self.__ip_header = bytes


        self.__info = bin(int(self.__ip_header.hex()[:3], 16))[2:]
        self.__frag_info = self.__ip_header[4:8]

        self.version = int('0b' + self.__info[:3], 2)
        if self.version == 4:

            self.ihl = int('0b' + self.__info[3:7], 2)
            self.tos_dcsp = self.__info[7:11]
            self.tos_ecn = self.__info[11:13]

            self.congest = int('0b' + self.__info[13:15].zfill(4), 2)
            self.len = self.__info[15:]

            self.__frag_info = bin(int(self.__ip_header.hex()[4:8], 16))[2:]
            self.frag_id = int('0b' + self.__frag_info[:15], 2)
            self.flags = int('0b' + self.__frag_info[15:18].zfill(4), 2)
            self.frag_offset = int('0b' + self.__frag_info[18:].zfill(32), 2)

            self.__pkt_info = self.__ip_header[8:12]
            self.ttl = int(self.__pkt_info[:1].hex(), 16)
            self.proto = int(self.__pkt_info[1:2].hex(), 16)
            self.hdr_cksum = self.__pkt_info[2:].hex()

            self.src_ip = socket.inet_ntoa(self.__ip_header[12:16])
            self.dst_ip = socket.inet_ntoa(self.__ip_header[16:20])

            self.options = None
            if self.ihl > 5:
                self.options = self.__ip_header[20:15+self.ihl]
        elif self.version == 6:
            self.traff_class = self.__info[3:11]
            self.flow_lbl = self.__info[11:]

            self.payload_len = int(self.__frag_info[:2].hex(), 16)
            self.next_header = int(self.__frag_info[2:3].hex(), 16)
            self.hop_limit = int(self.__frag_info[3:].hex(), 16)

            self.src_ip = fmt_ip6addr(self.__ip_header[8:24].hex())
            self.dst_ip = fmt_ip6addr(self.__ip_header[24:40].hex())

    def __repr__(self):
        if self.version == 4:
            return "VERSION: {}\nINTERNET HDR LENGTH: {}\nTOS: {} {}\n" \
                   "CONGESTION: {}\nLEN: {}\nFRAG_ID: {}\nFLAGS: {}\n" \
                   "FRAG_OFFSET: {}\nTTL: {}\nPROTO: {}\nHDR_CKSUM: {}" \
                   "\nSRC_IP: {}\nDST_IP: {}\nOPTIONS: {}\n".format(self.version,
                                                                   self.ihl,
                                                                   self.tos_dcsp,
                                                                   self.tos_dcsp,
                                                                   self.congest,
                                                                   self.len,
                                                                   self.frag_id,
                                                                   self.flags,
                                                                   self.frag_offset,
                                                                   self.ttl,
                                                                   self.proto,
                                                                   self.hdr_cksum,
                                                                   self.src_ip,
                                                                   self.dst_ip,
                                                                   self.options)
        if self.version == 6:
            return "VERSION: {}\nTRAFFIC_CLASS: {}\nPAYLOAD_LEN: {}\nNEXT_HEADER: {}\n" \
                   "HOP_LIMIT: {}\nSRC_IP: {}\nDST_IP: {}\n".format(self.version,
                                                                    self.traff_class,
                                                                    self.payload_len,
                                                                    self.next_header,
                                                                    self.hop_limit,
                                                                    self.src_ip,
                                                                    self.dst_ip)

class ArpData:

    def __init__(self, bytes):

        # Retrieve ethernet encapsulation data
        self.__arp_hdr = bytes

        # Slice ARP header into separate bytes objects
        self.hw_type = ''.join(map(str, unpack('BB', self.__arp_hdr[:2])))
        self.proto_type = self.__arp_hdr[2:4].hex()
        self.hw_addr_len = int(self.__arp_hdr[4:5].hex(), 16)
        self.proto_addr_len = int(self.__arp_hdr[5:6].hex(), 16)
        self.ope = int(self.__arp_hdr[6:8].hex(), 8)

        self.src_hw_addr = fmt_macaddr(self.__arp_hdr[8:8+self.hw_addr_len].hex())
        self.src_proto_addr = '.'.join(map(str, unpack('BBBB', self.__arp_hdr[8+self.hw_addr_len:8+self.hw_addr_len+self.proto_addr_len])))
        self.dst_hw_addr = fmt_macaddr(self.__arp_hdr[8+self.hw_addr_len+self.proto_addr_len:8+2*self.hw_addr_len+self.proto_addr_len].hex())
        self.dst_proto_addr = self.__arp_hdr[8+2*self.hw_addr_len+self.proto_addr_len:8+2*self.hw_addr_len+2*self.proto_addr_len].hex()
        if len(self.dst_proto_addr) != 0:
            self.dst_proto_addr = '.'.join(map(str, unpack('BBBB', self.__arp_hdr[8+2*self.hw_addr_len+self.proto_addr_len:8+2*self.hw_addr_len+2*self.proto_addr_len])))

    def __repr__(self):
        return "HW_TYPE: {}\nPROTO_TYPE: {}\nHW_ADDR_LEN: {}\nPROTO_ADDR_LEN: {}\nOPE: {}\nSRC_HW_ADDR:" \
               " {}\nSRC_PROTO_ADDR: {}\nDST_HW_ADDR: {}\nDST_PROTO_ADDR: {}".format(self.hw_type,
                                                                                     self.proto_type,
                                                                                     self.hw_addr_len,
                                                                                     self.proto_addr_len,
                                                                                     self.ope,
                                                                                     self.src_hw_addr,
                                                                                     self.src_proto_addr,
                                                                                     self.dst_hw_addr,
                                                                                     self.dst_proto_addr)

def fmt_macaddr(mac_addr):
    # Retrieve hex form of mac address
    t = iter(mac_addr)
    # Return Unix-like mac address in the form ff:ff:ff:ff:ff:ff
    return ':'.join(a+b for a,b in zip(t, t))

def fmt_ip6addr(ip6_addr):
    # Retrieve hex form of mac address
    t = iter(ip6_addr)
    # Return Unix-like mac address in the form ff:ff:ff:ff:ff:ff
    return ':'.join(a+b for a,b in zip(t, t))

def main():
    s = socket.socket(
        socket.AF_PACKET,
        socket.SOCK_RAW,
        socket.htons(3)
    )
    frameCount=0

    s.bind(('eth2', 3))

    while True:
        message = s.recv(1024)

        eth_header = L2Data(message[:14])
        eth_payload = message[14:-4]

        print()
        print('-'*100)
        print("Frame number: {}".format(frameCount))
        print(repr(eth_header))

        if eth_header.eth_type in ['0800','86dd']:
            ip_req = IPData(eth_payload)
            print()
            print(repr(ip_req))
        elif eth_header.eth_type == '0806':
            arp_req = ArpData(eth_payload[:])
            print()
            print(repr(arp_req))

        frameCount+=1

if __name__ == '__main__':
    main()
