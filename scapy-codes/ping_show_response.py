#!/usr/bin/env python

# Don't forget sniff traffic in the 10.50.94.100 server with the following command:
# tcpdump -n -e -A -i em0 host 10.50.63.228 and not port 22
import sys
from scapy.all import sr1,IP,ICMP

ipadd = raw_input('Please enter IP address: ')

pingrespconst=sr1(IP(dst=ipadd)/ICMP())
if pingrespconst:
    pingrespconst.show()
