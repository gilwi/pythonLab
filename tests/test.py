#!/usr/bin/python3

import socket

def main():
    s = socket.socket(
        socket.AF_PACKET,
        socket.SOCK_RAW,
        socket.htons(3)
    )
    frameCount=0

    s.bind(('eth0', 3))

    while True:
        message = s.recv(256)

        print("This is packet number :", frameCount)
        print(message)

        frameCount+=1
        if frameCount > 1000:
            exit()

if __name__ == '__main__':
    main()
