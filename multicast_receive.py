# -*- coding: utf-8 -*-
"""
Created on Sat May 26 13:54:24 2018

@author: Christophe
"""

import socket
import struct
import cPickle as pickle

def recieve_broadcast():
    try:
        MCAST_GRP = '224.0.0.1'
        MCAST_PORT = 5007
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('', MCAST_PORT))  # use MCAST_GRP instead of '' to listen only
                                     # to MCAST_GRP, not all groups on MCAST_PORT
        mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
        
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        
        data = pickle.loads(sock.recv(1024000))
        
        return data
    except:
        print "port probs already open"

if __name__ == "__main__":
    while True:
        data = recieve_broadcast()
        print data
        print type(data)