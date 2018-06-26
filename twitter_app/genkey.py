#!/usr/bin/python

import sys
import struct

filename_in = sys.argv[1]
filename_out = sys.argv[2]

filein = open(filename_in, "r")
fileout = open(filename_out, "wb")

while True:
    ch = filein.read(1)

    if not ch :
        break

    data = struct.pack("i", ord(ch))
    fileout.write(data)

filein.close()
fileout.close()

