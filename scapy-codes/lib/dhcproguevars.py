import sys
from scapy.all import Ether,IP,UDP,BOOTP,DHCP,ARP,conf,get_if_raw_hwaddr

fam, hw = get_if_raw_hwaddr(conf.iface)
bcast=Ether(dst="ff:ff:ff:ff:ff:ff")
ipbcast=IP(src='0.0.0.0', dst='255.255.255.255')
dhcpclisrvports=UDP(sport=68, dport=67)
dhcpproto=BOOTP(chaddr=hw)
dhcpoption=DHCP(options=[('message-type', 'discover'), 'end'])
