#!/usr/bin/env python3 
# LARGE KITTEN
# TODO:  
#   * Add tls? 
#   * Add a builtin? Maybe like a download and upload function? 


import struct
import readline
import argparse
import socket

class sock(socket.socket):
    def __init__(self, family=socket.AF_INET, type=socket.SOCK_STREAM):
        super().__init__(family, type)
        return

    def recv_all(self, chunk_size: int) -> bytes:
        #Recieve all the data. Never know how much you'll get.
        sock_data= []
        while True:
            sock_buf = self.recv(chunk_size)
            if 0 < len(sock_buf) < chunk_size: 
                sock_data.append(sock_buf)
                resp_data = sock_data 
                sock_data = []
                break
            else: 
                sock_data.append(sock_buf) 
        return b''.join(resp_data)


def send_cmd(sock: socket, cmd: bytes) -> None:
    sock.sendall(cmd.encode())
    data = sock.recv_all(4096)
    print(data.decode())
    return

def main(host: tuple[str, int] = None) -> None:
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', default='127.0.0.1', type=str, help='Ip to connect to.')
    parser.add_argument('-p', default=8080, type=int, help='Port to connect to.')
    args = parser.parse_args()
    host = (args.i, args.p)
    

    readline.parse_and_bind('tab: complete')
    socket.setdefaulttimeout(5.0)
    s = sock(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(host)

    while True:
        cmd = input("rlwrap-shell > ")
        if cmd == '': 
            continue
        if cmd.startswith('='):
            match cmd[1:]:
                case 'help':
                    print('[*] Commands!:\nhelp\nexit')
                    continue
                case 'exit':
                    s.close()
                    print('[*] Bye')
                    exit()
                case _: 
                    print('[!] Command doesnt exist!') 
                    continue

        cmd = cmd + '\n'
        try: 
            send_cmd(s, cmd)
        except TimeoutError:
            print('[!] Something went wrong with your shell command. It may not exist.')
            continue

if __name__ == "__main__":
    main()
