import os
import smtplib
import paramiko

codepath = os.getcwd()
outputdir = codepath+'/outdir/'
frommail = "ultra.notificator@gmail.com"
fromemailpass = "Ultra123@"
tomail= "jamal.shahverdiev@gmail.com"
iplist = open('iplist', 'r')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def emailsend(frommail, fromemailpass, tomail, mac, vlanID):
    message =  """From: Ultra Notificator <{2}>
To: Qurbanov Araz <{3}>
Subject: New MAC address for VLAN {1}
MAC address "{0}" is not founded in "StaticMacs" file""".format(mac, vlanID, frommail, tomail)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(frommail, fromemailpass)
    server.sendmail(frommail, tomail, message)
    server.quit()

def macget(vlanID, ip):
    stdin, stdout, stderr = ssh.exec_command('show mac address-table vlan '+vlanID+'')
    output = stdout.readlines()

    with open(outputdir+''+ip+'', 'wb') as switchout:
        switchout.write(''.join(output))

def filterMAC(ip, vlanID):
    os.system('cat '+outputdir+'/'+ip+' | grep -v -i ALL | grep '+vlanID+' | awk \'{print $2 }\' >> '+outputdir+'/MAC.result')

def getallMACs(ip, vlanID):
    os.system('cat '+outputdir+'/'+ip+' | grep -v -i ALL | grep '+vlanID+' | awk \'{print $2 }\' >> '+outputdir+'/MAC.list')

