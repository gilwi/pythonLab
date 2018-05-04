

class EthData:

    def __init__(self, bytes):

        # Translate bytes sequence to slice-able string
        self.bytes = bytes

        # Retrieve ethernet encapsulation data
        self.eth_header = self.bytes[:14]
        self.eth_fcs = self.bytes[-4:]

        # Retrieve indiviual group of bytes from ethernet header
        self.mac_dst = fmt_macaddr(self.eth_header[:6].hex())
        self.mac_src = fmt_macaddr(self.eth_header[6:-2].hex())
        self.eth_type = self.eth_header[-2:].hex()


def fmt_macaddr(mac_addr):
    t = iter(mac_addr)
    return ':'.join(a+b for a,b in zip(t, t))






def main():
    pass


if __name__ == '__main__':
    main()