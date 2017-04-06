#!/usr/bin/env python
from scapy.all import *

fam,hw = get_if_raw_hwaddr("em0")
pktboot = Ether(src=hw, dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0", dst="255.255.255.255")/UDP(sport=68, dport=67)/BOOTP(chaddr=hw)
conf.checkIPaddr = False
pktoff = srp1(pktboot/DHCP(options=[("message-type","discover"),"end"]), timeout=2,iface="em0")

#print("op =", pktoff[BOOTP].op, ", yiaddr =", pktoff[BOOTP].yiaddr, ", options=", pktoff[DHCP].options)
#pktask = srp1(pktboot/DHCP(options=[("message-type","request"),("server_id","10.0.0.1"),("requested_addr","10.0.0.112"),"end"]),timeout=2,iface="em0")

for i in range(2, 255):
    srp1(pktboot/DHCP(options=[("message-type","request"),("server_id","10.0.0.1"),("requested_addr",'10.0.0.'+str(i)+''),"end"]),timeout=2,iface="em0")

#print(pktask[DHCP].options)

