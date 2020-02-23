#!/usr/bin/python

import socket
import time
import argparse

def SendCommandToVolumeUp (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send('\x0D\x21\x31\x4d\x56\x4c\x55\x50\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandToVolumeUpPlus (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send('\x0D\x21\x31\x4d\x56\x4c\x55\x50\x31\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandToVolumeDown (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send('\x0D\x21\x31\x4d\x56\x4c\x44\x4f\x57\x4e\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandToVolumeDownPlus (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send('\x0D\x21\x31\x4d\x56\x4c\x44\x4f\x57\x4e\x31\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandGetPowerStatus (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send('\x0D\x2a\x70\x6f\x77\x3d\x3F\x23\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    if repr(data) == "'>*pow=?#\\r\\r\\n*POW=OFF#\\r\\n'" or repr(data) == "'*POW=OFF#\\r\\n'" :
        print "0"
    elif repr(data) == "'>*pow=?#\\r\\r\\n*POW=ON#\\r\\n'" or repr(data) == "'*POW=ON#\\r\\n'" :
        print "1"

parser = argparse.ArgumentParser()
parser.add_argument ("IPAddress", help = "IP Address of Projector")
parser.add_argument ('Port', help = "Port of Projector")
parser.add_argument ("Command", help = "volup is to increase volume, voldown is to decrease volume, etc.", choices = ["volup", "volupplus", "voldown", "voldownplus"])

args = parser.parse_args()

if args.Command == 'volup' :
    SendCommandToVolumeUp ( args.IPAddress, int(args.Port) ) #Relays 1 permanent on
elif args.Command == 'volupplus' :
    SendCommandToVolumeUpPlus ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'voldown' :
    SendCommandToVolumeDown ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'voldownplus' :
    SendCommandToVolumeDownPlus ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
    #return pwrstatus

#ReturnValue = SendCommandToRelays ('\x0D\x2a\x70\x6f\x77\x3d\x6f\x6e\x23\x0D') #ON
#ReturnValue = SendCommandToRelays ('\x0D\x2a\x70\x6f\x77\x3d\x6f\x66\x66\x23\x0D') #OFF
#ReturnValue = SendCommandToRelays ('\x0D\x2a\x70\x6f\x77\x3d\x3F\x23\x0D') #POWER STATUS
#print('Received', repr(ReturnValue))
