#!/usr/bin/env python
import os
import sys

def getMessage(command):
    mess = ""
    for i in range(2, len(command)):
        mess += command[i]
        mess += " "
    return (mess)

command = sys.argv

commit = getMessage(command)

print(commit)

os.popen("git add --all")
os.popen("git commit -m \"" + commit + "\"")
os.popen("git push origin master")
