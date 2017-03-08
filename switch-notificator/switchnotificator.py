#!/usr/bin/env python
import os
import sys
sys.path.insert(0, './lib')
from varsfuncs import *

if os.path.exists(codepath+'/StaticMacs') and os.path.getsize(codepath+'/StaticMacs') > 0:
    pass
else:
    print('File "StaticMacs" does not exists or empty!!!')
    print('To use "switchnotificator.py" script you must define static MAC address list in the "StaticMacs" file...')
    print('If you want define static mac list then, connect all your computers to you switch devices and use "createstaticmacs.py" script!!!')
    sys.exit()

if len(sys.argv) < 4:
    sys.exit('Usage: {} switchusername switchpassword vlanID'.format(sys.argv[0]))
else:
    pass

with open('iplist', 'r') as iplist:
    for ip in iplist.readlines():
        ssh.connect(''.join(ip.split()), port=22, username=sys.argv[1], password=sys.argv[2], look_for_keys=False, allow_agent=False)
        macget(sys.argv[3], ''.join(ip.split()))
        filterMAC(''.join(ip.split()), sys.argv[3])

with open(outputdir+'/MAC.result', 'r') as macresult:
    for line in macresult.readlines():
        with open(codepath+'/StaticMacs') as smacs:
            if line in smacs:
                pass
            else:
                emailsend(frommail, fromemailpass, tomail, line.replace('\n', ''), sys.argv[3])
                os.system('rm -rf '+outputdir+'/*')

ssh.close()
