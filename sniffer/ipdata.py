from struct import unpack
import socket

class IpData:

    def __init__(self, bytes):

        # Retrieve ethernet encapsulation data
        self.__ip_header = bytes

        # Retrieve formatted string corresponding to
        # ip header information
        self.info = bin(int(self.__ip_header.hex()[:4], 16))[2:]
        # Get ip version number
        self.version = int('0b'+self.info[:3], 2)


        self.frag_info = self.__ip_header[4:8]
        self.pkt_info = self.__ip_header[8:12]

        self.src_addr = socket.inet_ntoa(self.__ip_header[12:16])
        self.dst_addr = socket.inet_ntoa(self.__ip_header[16:20])

        self.options = None


        # self.version = self.ip_header[0:3]
        # self.hdr_len = self.ip_header[4:8]
        # self.tos = self.ip_header[8:14]
        # self.ecn = self.ip_header[14:16]
        # self.pkt_len = self.ip_header[16:32]
        # self.frag_id = self.ip_header[32:48]
        # self.flags = self.ip_header[48:51]
        # self.frag_offset = self.ip_header[51:64]
        # self.ttl = self.ip_header[64:72]
        # self.proto = self.ip_header[72:80]
        # self.hdr_cksum = self.ip_header[80:96]
        # self.src_addr = self.ip_header[96:128]
        # self.dst_addr = self.ip_header[128:160]

def main():
    pass


if __name__ == '__main__':
    main()