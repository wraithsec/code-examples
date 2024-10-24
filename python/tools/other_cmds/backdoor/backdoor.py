#!/usr/bin/env python3
import socket
import struct
import os

def main():
#    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
#    
#    while True:
#        pkt = s.recv(65565)
#        pkt = pkt[0]
#        ip_header = pkt[0:20]
#        iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
#        print(iph)

    rs = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    rs.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    print("[+] Listening for packets...")
    while True:
        pkt = rs.recvfrom(2048)
        icmp_type = struct.unpack('!B', pkt[0][20])
        print('icmp: ', icmp_type1)
        vihl, tos, total_len, identification, flags_offset, TTL, proto, header_checksum, s_ip, d_ip = struct.unpack('! B B H H H B B H 4s 4s', pkt[:20])
        if icmp_type == 8:
            print(s_ip, d_ip)
            print(TTL)
    return None



if __name__ == "__main__":
    main()
