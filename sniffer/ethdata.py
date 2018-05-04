import struct

class EthData:
    # Frame Session counter
    frameCount = 0

    def __init__(self, bytes):
        # Translate bytes sequence to slice-able string
        self.bytes = bytes

        # Retrieve ethernet encapsulation data
        self.ethHeader = self.bytes[:14]
        self.ethFooter = self.bytes[-4:]

        # Retrieve indiviual group of bytes from ethernet header
        self.macDst = self.ethHeader[:6]
        self.macSrc = self.ethHeader[6:-2]
        self.ethType = self.ethHeader[-2:]





def main():
    frame = ethData()


if __name__ == '__main__':
    main()