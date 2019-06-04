from __future__ import print_function

import sys
import cv2
import socket

HOST = "127.0.0.1 1234"
PEN = 0

def movePenTo0_0():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 1234
    BUFFER_SIZE = 1024
    MESSAGE = str.encode("PEN {}\n".format(PEN))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE).decode("utf-8").replace("\n", "")
    s.close()
    
    data = data.split()
    x = int(data[2])
    y = int(data[3])
    black="000000"

    for i in range(x):
        print("MOVE {} -1 0 {}".format(PEN, black))
    for i in range(y):
        print("MOVE {} 0 -1 {}".format(PEN, black))

def printImageFromPathToStdOut(filePath):
    image = cv2.imread(filePath)
    imageWidth = len(image)
    imageHeight = len(image[0])
    x = 0
    y = 0
    while(y < imageWidth):
        if (y % 2 == 0):
            while (x < imageHeight - 1): # Move to compelete right
                hexColor = '%02x%02x%02x' % tuple(image[x, y])
                print("MOVE {} 0 1 {}".format(PEN, hexColor))
                x += 1
        else:
            while (x > 0): # Move to compelete left
                hexColor = '%02x%02x%02x' % tuple(image[x, y])
                print("MOVE {} 0 -1 {}".format(PEN, hexColor))
                x -= 1
        hexColor = '%02x%02x%02x' % tuple(image[x, y]) # Move 1px down
        print("MOVE {} 1 0 {}".format(PEN, hexColor))
        y += 1

# MAIN
if len(sys.argv) != 2:
    print("Must have 1 arguments: filepath of image ", file=sys.stderr)
    sys.exit()

movePenTo0_0()
printImageFromPathToStdOut(sys.argv[1])
