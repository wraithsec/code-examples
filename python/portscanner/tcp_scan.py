#!/usr/bin/env python3 
import argparse
import threading
import socket
import os 
import re

        
    
class C():
    pre = '\033'
    clear = pre + '[1;0m'
    green = pre + '[1;92m'
    red = pre + '[1;91m'
    
def cprint(msg):
    if msg.startswith('[+]'):
        print(C.green + msg[:3] + C.clear + msg[3:])
    elif msg.startswith('[-]'):
        print(C.red + msg[:3] + C.clear + msg[3:])
    else:
        print(msg)
    
    

def main(ips, port):
    for ip in ips:
        #for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            resp = s.connect_ex((ip, port))
            s.close()
            if resp == 0:
                cprint(f'[+] {ip}:{port} is open.')
            else:
                cprint(f'[-] {ip}:{port} is closed.')
        except exception as e :
            cprint(f'[-] Unhandled socket error:\n {e}')
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Port scanner') 
    parser.add_argument('-p', '--ports', metavar='PORTS', type=int, required=True, help='TODO: Take start-end, port,port,port or -p port -p port' )
    parser.add_argument('ips', metavar='IPS', nargs='+', type=str)
    args = parser.parse_args()
    main(args.ips, args.ports)
    
    
