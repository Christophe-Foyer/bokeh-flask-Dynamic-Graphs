# -*- coding: utf-8 -*-
"""
Created on Sat May 26 13:54:55 2018

@author: Christophe
"""
import cPickle as pickle

def cast_data(data):

    data_string = pickle.dumps(data, -1) 
    
    import socket
    
    MCAST_GRP = '224.0.0.1'
    MCAST_PORT = 5007
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    sock.sendto(data_string, (MCAST_GRP, MCAST_PORT))
    sock.close()
    
if __name__ == "__main__":
    from bokeh.sampledata.sea_surface_temperature import sea_surface_temperature
    from bokeh.models import ColumnDataSource
#    data = {'a':1, 'b':2}
    data = sea_surface_temperature.copy()
    print data.head(5)
    print len(data)
    cast_data(data.iloc[15100:15199])