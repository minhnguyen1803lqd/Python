#!/usr/bin/env python
import os
import sys

def getMessage(command):
    mess = ""
    for i in range(2, len(command)):
        mess += command[i]
    return (mess)

command = sys.argv

commit = getMessage(command)

os.popen("git add --all")
os.popen("git commit -m " + commit)
os.popen("git push origin master")