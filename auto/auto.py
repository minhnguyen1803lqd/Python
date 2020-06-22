#!/usr/bin/env python
import os
import sys

templates = os.listdir("/mnt/c/users/nguye/code/cp/templates")
usersPath = "/mnt/c/users/nguye/code/cp/judserver/users"
testsPath = "/mnt/c/users/nguye/code/cp/judserver/tests"
command = sys.argv

def getFunction(command):
    return (command[1])

def getArgs(command):
    res = []
    for i in range(2, len(command)):
        res.append(command[i])
    return (res)

def makeFunc(args):
    path = args[0]
    name = ""
    for i in range(len(path) - 1, -1, -1):
        if path[i] == '/':
            break
        name = path[i] + name
    os.popen("mkdir " + path)
    for file in templates:
        if (file == "task.cpp"):
            os.popen("cp ~/bin/templates/" + file + " " + path + "/" + name + ".cpp")
        elif (file == "task.inp"):
            os.popen("cp ~/bin/templates/" + file + " " + path + "/" + name + ".inp")
        else:
            os.popen("cp ~/bin/templates/" + file + " " + path)

def uploadFunc(args):
    user = args[0]
    path = args[1]
    name = ""
    for i in range(len(path) - 1, 0, -1):
        if path[i] == '/':
            break
        name = path[i] + name
    os.popen("cp " + path + "/" + name + ".cpp " + usersPath + "/" + user)

def generateFunc(args):
    path = args[0]
    query = args[1]
    name = ""
    for i in range(len(path) - 1, 0, -1):
        if path[i] == '/':
            break
        name = path[i] + name

    os.popen("g++ " + path + "/generater.cpp -o " + path + "/generater")
    os.popen("g++ " + path + "/bruce.cpp -o " + path + "/bruce")
    os.mkdir(path + "/" + name)

    for i in range(0, int(query)):
        num = str(i)
        if (i < 10):
            num = '0' + num
        subPath = path + "/" + name + "/test" + num
        os.mkdir(subPath)
        os.popen("./" + path + "/generater")
        os.popen("./" + path + "/bruce")
        os.popen("mv " + name + ".inp " + subPath + "/" + name + ".inp")
        os.popen("mv " + name + ".ans " + subPath + "/" + name + ".out")

    os.popen("cp -r " + path + "/" + name + " " + testsPath)

func = getFunction(command)
args = getArgs(command)

if (func == "make"):
    makeFunc(args)
elif (func == "upload"):
    uploadFunc(args)
elif (func == "generate"):
    generateFunc(args)
