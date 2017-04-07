from scapy.all import get_if_raw_hwaddr,Ether,IP,UDP,BOOTP,conf

netcard = raw_input("Please enter network card name: ")
fam,hw = get_if_raw_hwaddr(netcard)

bcast=Ether(dst="ff:ff:ff:ff:ff:ff")
ipbcast=IP(src='0.0.0.0', dst='255.255.255.255')
dhcpclisrvports=UDP(sport=68, dport=67)
dhcpproto=BOOTP(chaddr=hw)
pktboot = bcast/ipbcast/dhcpclisrvports/dhcpproto
conf.checkIPaddr = False

