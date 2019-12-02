#!/usr/bin/python

import socket
import time
import argparse

def SendCommandToPowerOn (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x2a\x70\x6f\x77\x3d\x6f\x6e\x23\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandToPowerOff (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x2a\x70\x6f\x77\x3d\x6f\x66\x66\x23\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandGetPowerStatus (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x2a\x70\x6f\x77\x3d\x3F\x23\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    if repr(data) == "b'>*pow=?#\\r\\r\\n*POW=OFF#\\r\\n'" or repr(data) == "b'*POW=OFF#\\r\\n'" :
        print("0")
    elif repr(data) == "b'>*pow=?#\\r\\r\\n*POW=ON#\\r\\n'" or repr(data) == "b'*POW=ON#\\r\\n'" :
        print("1")
    else:
        print("Unexpected reply from device")

parser = argparse.ArgumentParser()
parser.add_argument ("IPAddress", help = "IP Address of Projector")
parser.add_argument ('Port', help = "Port of Projector")
parser.add_argument ("Power", help = "on is to power on, off is to power off, status is to get power status (0 = on, 1 = off)", choices = ["on", "off", "status"])

args = parser.parse_args()

if args.Power == 'on' :
    SendCommandToPowerOn ( args.IPAddress, int(args.Port) ) #Relays 1 permanent on
elif args.Power == 'off' :
    SendCommandToPowerOff ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Power == 'status' :
    SendCommandGetPowerStatus ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
    #return pwrstatus

#ReturnValue = SendCommandToRelays ('\x0D\x2a\x70\x6f\x77\x3d\x6f\x6e\x23\x0D') #ON
#ReturnValue = SendCommandToRelays ('\x0D\x2a\x70\x6f\x77\x3d\x6f\x66\x66\x23\x0D') #OFF
#ReturnValue = SendCommandToRelays ('\x0D\x2a\x70\x6f\x77\x3d\x3F\x23\x0D') #POWER STATUS
#print('Received', repr(ReturnValue))
