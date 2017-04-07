#! /usr/bin/env python

# Don't forget sniff traffic in the 10.50.94.100 server with the following command:
# tcpdump -n -e -A -i em0 host 10.50.63.228 and not port 22
from scapy.all import send, IP, ICMP, srloop

ipadd = raw_input('Please enter IP address to ping: ')
for i in range(1, 2):
    #print('Sent count: {0}'.format(i))
    send(IP(src="",dst="{0}".format(ipadd))/ICMP()/"""
            USUDUM AY USUDUM,
            DAGDAN ALMA DASIDIM,
            ALMACIQIM ADLILAR,
            MENE ZULUM VERDILER.
            MEN ZULUMDAN BEZEREM,
            DERIN QUYU QAZARAM.
            DERIN QUYU BES KECI,
            HANI BUNUN ERKECI?
            ERKECI QAYA BASINDA.
            HA CAQIRDIM GELMEDI,
            HU CAQIRDIM GELMEDI.
            DARI SEPDIM YEMEDI.
            DARI QAZANDA QAYNAR.
            QENBER BUCAQDA OYNAR.
            QENBER GETDI ODUNA.
            QARGI BATDI BUDUNA.
            QARGI DEYIL QAMISDI,
            BES BARMAGIM GUMUSDU.
            GUMUSU VERDIM TATA.
            TAT MENE QANAD VERDI,
            QANATLANDIM UCMAGA,
            HEQ QAPISIN ACMAGA.
            HEQ QAPISI KILITLI,
            KILIT BABAM BELINDE.
            BABAM ELEF YOLUNDA.
            ELEF YOLU SERBESER,
            ICINDE MEYMUN GEZER.
            MEYMUNUN BALALARI,
            MENI GORUB AGLADI,
            TUMANINA QIGLADI.
            """)
#srloop(IP(dst="{0}".format(ipadd))/ICMP(), count=4)
