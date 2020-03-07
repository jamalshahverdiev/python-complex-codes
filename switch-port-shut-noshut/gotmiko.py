#!/usr/bin/env python3

import getpass
import sys
from netmiko import ConnectHandler

if len(sys.argv) < 6:
    sys.exit('Usage: {} username password enpass first_port_number second_port_number'.format(sys.argv[0]))
else:
    pass

#user = input('Username: ')
#password = getpass.getpass()
#enable_pass = getpass.getpass(prompt='Enter enable password: ')
input_command = '{} {}'.format('show interfaces status | inc', sys.argv[4])
output_command = '{} {}'.format('show interfaces status | inc', sys.argv[4])
commandToNoShut = ['{} {}'.format('interface ', sys.argv[5]), 'no shutdown']
commandToShut = ['{} {}'.format('interface ', sys.argv[5]), 'shutdown']
user = sys.argv[1]
password = sys.argv[2]
enable_pass = sys.argv[3]
devices_ip = ['192.168.20.80']

for ip in devices_ip:
    print('connection to device {}'.format(ip))
    device_params = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': user,
        'password': password,
        'secret': enable_pass
    }

    with ConnectHandler(**device_params) as ssh:
        ssh.enable()

        first_port = ssh.send_command(input_command)
        if "disabled" in first_port:
            result = ssh.send_config_set(commandToNoShut)
            print(result)
        elif "notconnect" in first_port:
            result = ssh.send_config_set(commandToShut)
            print(result)
