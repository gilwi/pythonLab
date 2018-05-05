class EthData:

    def __init__(self, bytes):

        # Retrieve ethernet encapsulation data
        self.__eth_header = bytes[:14]
        # self.eth_fcs = self.bytes[-4:]

        # Retrieve formatted string corresponding to
        # ethernet header information
        self.mac_dst = fmt_macaddr(self.__eth_header[:6].hex())
        self.mac_src = fmt_macaddr(self.__eth_header[6:-2].hex())
        self.eth_type = self.__eth_header[-2:].hex()


def fmt_macaddr(mac_addr):
    # Retrieve hex form of mac address
    t = iter(mac_addr)
    # Return Unix-like mac address in the form ff:ff:ff:ff:ff:ff
    return ':'.join(a+b for a,b in zip(t, t))







def main():
    pass


if __name__ == '__main__':
    main()