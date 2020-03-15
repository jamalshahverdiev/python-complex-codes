#!/usr/bin/env python3

ips = ['192.168.9.70', '192.168.9.41', '192.168.9.40']

with open('access_list.txt', 'w') as filehandle:
    for listitem in ips:
        filehandle.write('%s\n' % listitem)

with open('access_list.txt', 'r') as filehandle:
    filecontents = filehandle.readlines()
    API_ALLOWED_IPS = list(map(lambda x:x.strip(),filecontents))

print(API_ALLOWED_IPS)
