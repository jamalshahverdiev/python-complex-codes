#!/usr/bin/env python
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import sys
sys.path.insert(0, './lib')
from dhcprequestvars import srp1, DHCP

##pktoff = srp1(pktboot/DHCP(options=[("message-type","discover"),"end"]), timeout=2,iface="em0")
##print("op =", pktoff[BOOTP].op, ", yiaddr =", pktoff[BOOTP].yiaddr, ", options=", pktoff[DHCP].options)

for i in range(2, 255):
    srp1(pktboot/DHCP(options=[("message-type","request"),("server_id","10.0.0.1"),("requested_addr",'10.0.0.'+str(i)+''),"end"]),timeout=2,iface=netcard)

##print(pktask[DHCP].options)

