#!/usr/bin/env python2.7

from bs4 import BeautifulSoup
import requests
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("usdeurmezennesi@gmail.com", "D0llareur0")

finsurl='http://fins.az/bank'

response = requests.get(finsurl)
respData = BeautifulSoup(response.content, "html.parser")
usd = respData.find('div', {'class': 'value'}).get_text()
eur = respData.find('div', {'class': 'value'}).find_next('div', {'class': 'value'}).get_text()

def printer_func(site, dollar, euro):
    return "%s saytindan istinad edilmishdir: " % str(site), "1 USD = %s AZN" % str(dollar), "1 EURO: %s AZN" % str(euro)

cbarurl='http://www.cbar.az/'
respcbar = requests.get(cbarurl)
cbrespData = BeautifulSoup(respcbar.content, "html.parser")
cbusd = cbrespData.find('span', {'class': 'item item_4'}).get_text()
cbeur = cbrespData.find('span', {'class': 'item item_4'}).find_next('span', {'class': 'item item_4'}).get_text()

faz = printer_func(str(finsurl), str(usd), str(eur))
caz = printer_func(str(cbarurl), str(cbusd), str(cbeur))

message = """From: Euro Dollar <usdeurmezennesi@gmail.com>
To: Email Author <email.author@example.com>
Subject: Euro Dollar mezennesi

%s %s, %s
%s %s, %s
""" % (faz[0], faz[1], faz[2], caz[0], caz[1], caz[2])

server.sendmail("usdeurmezennesi@gmail.com", "email.author@example.com", message)
server.quit()
