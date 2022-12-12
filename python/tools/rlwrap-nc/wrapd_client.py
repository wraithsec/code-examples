#!/usr/bin/env python3
'''
Something new I discovered you can use select to poll fds...
'''

import socket
import struct
import readline

# Create a socket object
s = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_TCP
)

# Prompt the user for the host and port
host = input('Enter the host: ')
port = int(input('Enter the port: '))


s.connect((host, port))
while True:
    cmd = input('KILO > ').encode('utf-8')
    print(cmd)
    #if cmd == b'qq': 
    #    print('[+] Bye') 
    #    s.close()
    #    break 
    data_to_send = struct.pack('!32s', cmd)
    print(data_to_send)
    s.sendall(data_to_send)

    data = s.recv(8192)
    if not data: 
        continue
    response += data
    received_data = struct.unpack('!32s', response)
    print(received_data.decode('utf-8'))
