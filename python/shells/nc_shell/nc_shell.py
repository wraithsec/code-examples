#!/usr/bin/env python3 
#LARGE KITTEN

import struct
import readline
import argparse
import socket


#class socket(socket.socket):
#    def recv_all(self):
#        buffer = self.recv(8192)
#        data = b''
#        while buffer is 
#        return


def recv_all(sock: socket) -> bytes:
    #Recieve all the data. Because we never know how
    sock_data= []
    while True:
        sock_buf = sock.recv(2048)
        if 0 < len(sock_buf) < 2048: 
            sock_data.append(sock_buf)
            break
        else: 
            sock_data.append(sock_buf) 
    return b''.join(sock_data)



def main(host: tuple[str, int]) -> None:
    readline.parse_and_bind('tab: complete')
    socket.setdefaulttimeout(5.0)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(host)

    while True:
        cmd = input("LAKI > ")
        if cmd == '': continue
        if cmd == 'help':
            print('* Commands')
            continue
        if cmd == 'exit':
            s.close()
            print('* Outta here')
            exit()
        cmd = cmd + '\n'
        #packed_cmd = struct.pack(">32s", cmd.encode())
        s.sendall(cmd.encode())
        data = recv_all(s)
        print(data.decode())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', default='127.0.0.1', help='Ip to connect to.')
    parser.add_argument('-p', default=8080, help='Port to connect to.')
    args = parser.parse_args()
    host = (args.i, args.p)
    main(host)