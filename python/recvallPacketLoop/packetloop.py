#!/usr/bin/env python3
# Just an attempt to write a recvall packetloop
msglen = 5700
recv_size = 1024
total_len = 5120


def recv_all(self, msglen):
    total_len=0;total_data=[]
    sock_buf='';recv_size=1024
    while total_len < msglen:
        sock_buf = self.conn.recv(recv_size)
        if recv_size > msglen:
            recv_size = msglen 
            total_len += len(sock_buf)
            total_data.append(sock_buf)
        total_len += len(sock_buf) 
        total_data.append(sock_buf)





