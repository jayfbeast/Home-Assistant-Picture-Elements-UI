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
    s.sendall(b'\x0D\x21\x31\x4d\x56\x4c\x55\x50\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandToVolumeUpPlus (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x4d\x56\x4c\x55\x50\x31\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandToVolumeDown (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x4d\x56\x4c\x44\x4f\x57\x4e\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandToVolumeDownPlus (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x4d\x56\x4c\x44\x4f\x57\x4e\x31\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandToVolumeMute (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x41\x4D\x54\x30\x31\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandToVolumeUnmute (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x41\x4D\x54\x30\x30\x0D')
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

#**************************************************************************************************************************************************
#SUBWOOFER CONTROL
#**************************************************************************************************************************************************

def SendCommandToVolumeDownSubwoofer (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x53\x57\x4C\x44\x4F\x57\x4E\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandToVolumeUpSubwoofer (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x53\x57\x4C\x55\x50\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandToTurnOffSubwoofer (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x53\x57\x4C\x2D\x31\x45\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandToSetHalfVolumeSubwoofer (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x53\x57\x4c\x30\x30\x30\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandToSetMaxVolumeSubwoofer (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x53\x57\x4c\x2b\x31\x38\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

#**************************************************************************************************************************************************
#REMOTE CONTROL
#**************************************************************************************************************************************************

def SendCommandRemoteControlMenu (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x4F\x53\x44\x4D\x45\x4E\x55\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandRemoteControlExit (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x4F\x53\x44\x45\x58\x49\x54\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandRemoteControlUp (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x4F\x53\x44\x55\x50\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandRemoteControlDown (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x4F\x53\x44\x44\x4F\x57\x4E\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandRemoteControlLeft (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x4F\x53\x44\x4C\x45\x46\x54\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandRemoteControlRight (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x4F\x53\x44\x52\x49\x47\x48\x54\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandRemoteControlEnter (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x4F\x53\x44\x45\x4E\x54\x45\x52\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandRemoteControlAudioAdjust (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x4F\x53\x44\x41\x55\x44\x49\x4F\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandRemoteControlVideoAdjust (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x4F\x53\x44\x56\x49\x44\x45\x4F\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandRemoteControlHome (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x4F\x53\x44\x48\x4F\x4D\x45\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandRemoteControlQuickSetup (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x4F\x53\x44\x51\x55\x49\x43\x4B\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data

def SendCommandRemoteControlInstaprevue (IPAddress, Port):
    TCP_IP = IPAddress #IP address of the relays
    TCP_PORT = Port #Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(b'\x0D\x21\x31\x4F\x53\x44\x49\x50\x56\x0D')
    data = s.recv(BUFFER_SIZE) #Response from Relays
    s.close()
    return data


parser = argparse.ArgumentParser()
parser.add_argument ("IPAddress", help = "IP Address of Projector")
parser.add_argument ('Port', help = "Port of Projector")
parser.add_argument ("Command", help = "volup is to increase volume, voldown is to decrease volume, etc.", choices = ["volup", "volupplus", "voldown", "voldownplus", "subvolup", "subvoldown", "subvoloff", "subvolhalf", "subvolmax", "SendCommandRemoteControlMenu", "SendCommandRemoteControlExit", "SendCommandRemoteControlUp", "SendCommandRemoteControlDown", "SendCommandRemoteControlLeft", "SendCommandRemoteControlRight", "SendCommandRemoteControlEnter", "SendCommandRemoteControlAudioAdjust", "SendCommandRemoteControlVideoAdjust", "SendCommandRemoteControlHome", "SendCommandRemoteControlQuickSetup", "SendCommandRemoteControlInstaprevue", "volmute", "volunmute"])

args = parser.parse_args()

if args.Command == 'volup' :
    SendCommandToVolumeUp ( args.IPAddress, int(args.Port) ) #Relays 1 permanent on
elif args.Command == 'volupplus' :
    SendCommandToVolumeUpPlus ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'voldown' :
    SendCommandToVolumeDown ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'voldownplus' :
    SendCommandToVolumeDownPlus ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'subvolup' :
    SendCommandToVolumeUpSubwoofer ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'volmute' :
    SendCommandToVolumeMute ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'volunmute' :
    SendCommandToVolumeUnmute ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'subvoldown' :
    SendCommandToVolumeDownSubwoofer ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'subvoloff' :
    SendCommandToTurnOffSubwoofer ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'subvolhalf' :
    SendCommandToSetHalfVolumeSubwoofer ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'subvolmax' :
    SendCommandToSetMaxVolumeSubwoofer ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'SendCommandRemoteControlMenu' :
    SendCommandRemoteControlMenu ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'SendCommandRemoteControlExit' :
    SendCommandRemoteControlExit ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'SendCommandRemoteControlUp' :
    SendCommandRemoteControlUp ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'SendCommandRemoteControlDown' :
    SendCommandRemoteControlDown ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'SendCommandRemoteControlLeft' :
    SendCommandRemoteControlLeft ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'SendCommandRemoteControlRight' :
    SendCommandRemoteControlRight ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'SendCommandRemoteControlEnter' :
    SendCommandRemoteControlEnter ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'SendCommandRemoteControlAudioAdjust' :
    SendCommandRemoteControlAudioAdjust ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'SendCommandRemoteControlVideoAdjust' :
    SendCommandRemoteControlVideoAdjust ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'SendCommandRemoteControlHome' :
    SendCommandRemoteControlHome ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'SendCommandRemoteControlQuickSetup' :
    SendCommandRemoteControlQuickSetup ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
elif args.Command == 'SendCommandRemoteControlInstaprevue' :
    SendCommandRemoteControlInstaprevue ( args.IPAddress, int(args.Port) ) #Relays 1 permanent off
    #return pwrstatus

#ReturnValue = SendCommandToRelays ('\x0D\x2a\x70\x6f\x77\x3d\x6f\x6e\x23\x0D') #ON
#ReturnValue = SendCommandToRelays ('\x0D\x2a\x70\x6f\x77\x3d\x6f\x66\x66\x23\x0D') #OFF
#ReturnValue = SendCommandToRelays ('\x0D\x2a\x70\x6f\x77\x3d\x3F\x23\x0D') #POWER STATUS
#print('Received', repr(ReturnValue))
