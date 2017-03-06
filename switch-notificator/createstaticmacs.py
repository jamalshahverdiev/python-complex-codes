#!/usr/bin/env python
import os
import paramiko

codepath = os.getcwd()
outputdir = codepath+'/outdir/'

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
    ssh.connect(''.join(ip.split()), port=22, username='switchuser', password='switchpass', look_for_keys=False, allow_agent=False)
    macget('823', ''.join(ip.split()))
    getallMACs(''.join(ip.split()), '823')

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
