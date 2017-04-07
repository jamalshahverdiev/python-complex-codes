#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import sendp, sniff
sys.path.insert(0, './lib')
from dhcproguevars import *

# Define a callback function for when DHCP packets are received
def dhcp_get_offer(pkt):
    # Check if the DHCP packet is a DHCP offer from DHCP server
    if DHCP in pkt and pkt[DHCP].options[0][1] == 2:
        print('DHCP server IP address: {0} MAC address: {1}'.format(pkt[IP].src, pkt[Ether].src))

# Packet structure of DHCP request
dhcp_request=(bcast/ipbcast/dhcpclisrvports/dhcpproto/dhcpoption)

# Only send the DHCP request in the channel layer(L2)
sendp(dhcp_request)

# Sniff for any DHCP packets and don't store them in the memory
sniff(prn=dhcp_get_offer, store=0)
