from struct import unpack
class ArpData:

    def __init__(self, bytes):

        # Retrieve ethernet encapsulation data
        self.__arp_hdr = bytes

        # Slice ARP header into separate bytes objects
        self.hw_type = unpack('BB', self.__arp_hdr[:2])
        self.proto_type = unpack('xB', self.__arp_hdr[2:4])
        self.hw_addr_len = self.__arp_hdr[4:5]
        self.proto_addr_len = self.__arp_hdr[5:6]
        self.ope = self.__arp_hdr[6:8]
        self.src_hw_addr = self.__arp_hdr[8:14]
        self.src_proto_addr = self.__arp_hdr[14:18]
        self.dst_hw_addr = self.__arp_hdr[18:24]
        self.dst_proto_addr = self.__arp_hdr[24:28]




def main():
    pass


if __name__ == '__main__':
    main()