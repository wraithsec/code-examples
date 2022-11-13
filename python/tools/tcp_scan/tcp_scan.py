#!/usr/bin/env python3 
import argparse
import threading
import socket
import sys 
import os 
import re

# TODO:     
# Add Threading
# Find a way to simplify parse_ports
# Add basic attempt to banner grab? 
        
    
class Color:
    pre = '\033'
    clear = pre + '[1;0m'
    green = pre + '[1;92m'
    red = pre + '[1;91m'
    

def cprint(msg):
    if msg.startswith('[+]'):
        print(Color.green + msg[:3] + Color.clear + msg[3:])
    elif msg.startswith('[-]'):
        print(Color.red + msg[:3] + Color.clear + msg[3:])
    else:
        print(msg)


def _parse_ports(ports: str) -> list[int]:
    parsed_ports = []
    ports = re.split(r',', ports)
    for p in ports:
        if '-' in p:
            tmp = re.split(r'-', p)
            tmp = [ int(_) for _ in  tmp ]
            if len(tmp) > 2: raise argparse.ArgumentTypeError(f'{p} not a valid argument')
            for _ in range(tmp[0], tmp[1]+1):
                parsed_ports.append(int(_))
        else:
            parsed_ports.append(int(p))
    return parsed_ports 


def main(ips, ports, timeout):
    for ip in ips:
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
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
    parser.add_argument('-t', '--timeout', metavar='T', type=int, help="Socket timeout value.", default=3)
    parser.add_argument('-p', '--ports', metavar='PORTS', type=_parse_ports)
    parser.add_argument('ips', metavar='IPS', nargs='+', type=str)
    args = parser.parse_args()
    main(args.ips, args.ports, args.timeout)
    
    
