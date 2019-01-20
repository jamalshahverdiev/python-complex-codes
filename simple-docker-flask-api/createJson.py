#!/usr/bin/env python

import os
import subprocess
import json

def returnArg(arg):
    my_dict = {"containerID": arg.split()[0], "imageName": arg.split()[1], "exposedPort": arg.split()[-2], "containerName": arg.split()[-1]}
    print(my_dict)
    return my_dict

for line in list(os.popen("docker ps | grep -v CONTAINER").readlines()):
    returnArg(line)
