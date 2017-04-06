#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
fam, hw = get_if_raw_hwaddr(conf.iface)

# Define a callback function for when DHCP packets are received
def dhcp_callback(pkt):
    # Check if the DHCP packet is a DHCP offer from DHCP server
    if DHCP in pkt and pkt[DHCP].options[0][1] == 2:
        print('DHCP server IP address: {0} MAC address: {1}'.format(pkt[IP].src, pkt[Ether].src))

# Construct the DHCP request
dhcp_request = (
    Ether(dst='ff:ff:ff:ff:ff:ff') /
    IP(src='0.0.0.0', dst='255.255.255.255') /
    UDP(sport=68, dport=67) /
    BOOTP(chaddr=hw) /
    DHCP(options=[('message-type', 'discover'), 'end'])
)

# Send the DHCP request
sendp(dhcp_request)

# Sniff for any DHCP packets
sniff(prn=dhcp_callback, store=0)
