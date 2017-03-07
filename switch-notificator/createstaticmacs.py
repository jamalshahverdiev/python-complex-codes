#!/usr/bin/env python
import os
import paramiko
import sys

codepath = os.getcwd()
outputdir = codepath+'/outdir/'

if len(sys.argv) < 3:
    sys.exit('Usage: {} switchusername switchpassword vlanID'.format(sys.argv[0]))
else:
    pass

def macget(vlanID, ip):
    stdin, stdout, stderr = ssh.exec_command('show mac address-table vlan '+vlanID+'')
    output = stdout.readlines()

    with open(outputdir+''+ip+'', 'wb') as switchout:
        switchout.write(''.join(output))

def getallMACs(ip, vlanID):
    os.system('cat '+outputdir+'/'+ip+' | grep -v -i ALL | grep '+vlanID+' | awk \'{print $2 }\' >> '+outputdir+'/MAC.list')


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

iplist = open('iplist', 'r')
for ip in iplist.readlines():
    ssh.connect(''.join(ip.split()), port=22, username=sys.argv[1], password=sys.argv[2], look_for_keys=False, allow_agent=False)
    macget(sys.argv[3], ''.join(ip.split()))
    getallMACs(''.join(ip.split()), sys.argv[3])

with open(outputdir+'/MAC.list', 'r') as dirtymacs:
    for line in dirtymacs.readlines():
        with open('StaticMacs', 'a') as macresult:
            if line in open(codepath+'/StaticMacs'):
                print('This line is exists in the StaticMacs file!!!')
            else:
                macresult.write(line)
                print('New line is written to the StaticMacs file!!!')
    os.system('rm -rf '+outputdir+'/MAC.list')

iplist.close()
ssh.close()
