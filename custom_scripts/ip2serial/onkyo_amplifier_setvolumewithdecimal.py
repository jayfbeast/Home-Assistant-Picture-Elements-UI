#!/usr/bin/python

import socket
import time
import argparse
import binascii as bs

def SendCommandToChangeVolume (IPAddress, Port, Volume):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80
    volumeInHex = hex(Volume*2)[2:]
    #print(volumeInHex)
    string = "!1MVL" + str(volumeInHex.upper())
    h = bs.hexlify(string.encode()).decode()
    subfinalstring = '\\x'.join(h[i:i+2] for i in range(0, len(h), 2))
    prefix = "\\x0D\\x"
    suffix = "\\x0D"
    finalstring = prefix + subfinalstring + suffix
    print(finalstring)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(finalstring)
    #s.send('\x0D\x21\x31\x4d\x56\x4c\x36\x34\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

parser = argparse.ArgumentParser()
parser.add_argument ("IPAddress", help = "IP Address of Projector")
parser.add_argument ('Port', help = "Port of Projector")
parser.add_argument ("Volume", help = "Set volume. Available values: 0 to 100")

args = parser.parse_args()

SendCommandToChangeVolume ( args.IPAddress, int(args.Port), int(args.Volume) )