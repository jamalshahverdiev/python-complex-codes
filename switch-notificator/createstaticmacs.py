#!/usr/bin/env python
import os
import sys
sys.path.insert(0, './lib')
from varsfuncs import *

if len(sys.argv) < 4:
    sys.exit('Usage: {} switchusername switchpassword vlanID'.format(sys.argv[0]))
else:
    pass

with open('iplist', 'r') as iplist:
    for ip in iplist.readlines():
        ssh.connect(''.join(ip.split()), port=22, username=sys.argv[1], password=sys.argv[2], look_for_keys=False, allow_agent=False)
        macget(sys.argv[3], ''.join(ip.split()))
        getallMACs(''.join(ip.split()), sys.argv[3])

with open(outputdir+'/MAC.list', 'r') as dirtymacs:
    for line in dirtymacs.readlines():
        with open('StaticMacs', 'a') as macresult:
            with open(codepath+'/StaticMacs') as smacs:
                if line in smacs:
                    print('This line is exists in the StaticMacs file!!!')
                else:
                    macresult.write(line)
                    print('New line is written to the StaticMacs file!!!')
    os.system('rm -rf '+outputdir+'/*')

ssh.close()

