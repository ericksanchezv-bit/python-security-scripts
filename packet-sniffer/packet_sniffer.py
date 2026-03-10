
'''
BLACK HAT PYTHON
SNIFFER EXPERIMENT

Packet Sniffer – Educational Network Traffic Analyzer

Captures raw IP packets using Python sockets and parses the IP header
to display source IP, destination IP, and protocol information. The
script aggregates packet counts to analyze basic network traffic patterns.

Based on examples from the book "Black Hat Python" by Justin Seitz.
Adapted for educational use and experimentation.

'''

import socket
import os

from prettytable import PrettyTable

# Get the HOST to Sniff From
hostname = socket.gethostname()
HOST = socket.gethostbyname(hostname)

#HOST = 'localhost'

import ipaddress
import struct

class IP:
    def __init__(self, buff=None):
        
        header = struct.unpack('<BBHHHBBH4s4s', buff)
        self.ver = header[0] >> 4
        self.ihl = header[0] & 0xF

        self.tos    = header[1]
        self.len    = header[2]
        self.id     = header[3]
        self.offset = header[4]
        self.ttl    = header[5]
        self.protocol_num = header[6]
        self.sum    = header[7]
        self.src    = header[8]
        self.dst    = header[9]
    
        # human readable IP addresses
        self.src_address = ipaddress.ip_address(self.src)
        self.dst_address = ipaddress.ip_address(self.dst)
    
        # map protocol constants to their names
        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}


def main():
    
    socket_protocol = socket.IPPROTO_IP
    
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST,0))
    
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    
    captureDict = {}
    
    for i in range(1,10000):
        
        packet     = sniffer.recvfrom(65565)  # Wait for Packet
        basePacket = packet[0]                # Extract Packet Data from tuple
        pckHeader  = basePacket[0:20]         # Extract the packet header
        
        ipOBJ = IP(pckHeader)                 # Create the IP Object
    
        # Lookup the protocol name
        try:
            protocolName = ipOBJ.protocol_map[ipOBJ.protocol_num]
        except:
            protocolName = "Unknown"
            
        print("SRC-IP  :", ipOBJ.src_address)
        print("DST-IP  :", ipOBJ.dst_address)
        print("Protocol:", protocolName)

        
        
        key = (str(ipOBJ.src_address), str(ipOBJ.dst_address), protocolName)
    
        
        if key in captureDict:
            captureDict[key] += 1
        else:
            captureDict[key] = 1
    
        
        tbl = PrettyTable(["Occurs", "SRC", "DST", "Protocol"])
    
        
        sorted_packets = sorted(captureDict.items(), key=lambda x: x[1], reverse=True)
    
        
        for (src, dst, proto), count in sorted_packets:
            tbl.add_row([count, src, dst, proto])
    
        print(tbl)
        
    tbl = PrettyTable(["Occurs", "SRC", "DST", "Protocol"])
    print(tbl.get_string(reversesort=True))
          
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

if __name__ == '__main__':
    main()
