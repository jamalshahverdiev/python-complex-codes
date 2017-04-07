#!/usr/bin/env python
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

# Same thing for tcpdump: tcpdump -n -e -i em0 arp
def arp_mon(pkt):
    if ARP in pkt and pkt[ARP].op in (1,2): #who-has or is-at
        #print(pkt[ARP].op)
        return pkt.sprintf("%ARP.psrc% %ARP.hwsrc%")

# Sniff only ARP packets and send packet as argument to the arp_monitor_callback
sniff(prn=arp_mon, filter="arp", store=0)
