#!/usr/bin/env python
import smtplib
import os
import paramiko

codepath = os.getcwd()
outputdir = codepath+'/outdir/'

if os.path.exists(codepath+'/StaticMacs') and os.path.getsize(codepath+'/StaticMacs') > 0:
    pass
else:
    print('File "StaticMacs" does not exists or empty!!!')
    print('To use "switchnotificator.py" script you must define static MAC address list in the "StaticMacs" file...')
    print('If you want define static mac list then, connect all your computers to you switch devices and use "createstaticmacs.py" script!!!')

if len(sys.argv) < 4:
    sys.exit('Usage: {} switchusername switchpassword vlanID'.format(sys.argv[0]))
else:
    pass

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("company.notificator@gmail.com", "CompanyEmailPASS")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def createMessage(mac, vlanID):
    global message
    message =  """From: Company Notificator <company.notificator@gmail.com>
To: Email To <email.to@gmail.com>
Subject: New MAC address for VLAN {1}
MAC address "{0}" is not founded in "StaticMacs" file""".format(mac, vlanID)

def macget(vlanID, ip):
    stdin, stdout, stderr = ssh.exec_command('show mac address-table vlan '+vlanID+'')
    output = stdout.readlines()

    with open(outputdir+''+ip+'', 'wb') as switchout:
        switchout.write(''.join(output))

def filterMAC(ip, vlanID):
    os.system('cat '+outputdir+'/'+ip+' | grep -v -i ALL | grep '+vlanID+' | awk \'{print $2 }\' >> '+outputdir+'/MAC.result')

iplist = open('iplist', 'r')
for ip in iplist.readlines():
    ssh.connect(''.join(ip.split()), port=22, username=sys.argv[1], password=sys.argv[2], look_for_keys=False, allow_agent=False)
    macget(sys.argv[3], ''.join(ip.split()))
    filterMAC(''.join(ip.split()), sys.argv[3])


with open(outputdir+'/MAC.result', 'r') as macresult:
    for line in macresult.readlines():
        if line in open(codepath+'/StaticMacs'):
            pass
        else:
            createMessage(line.replace('\n', ''), sys.argv[3])
            server.sendmail("company.notificator@gmail.com", "email.to@gmail.com", message)
            server.quit()
            os.system('rm -rf '+outputdir+'/*')

iplist.close()
ssh.close()
