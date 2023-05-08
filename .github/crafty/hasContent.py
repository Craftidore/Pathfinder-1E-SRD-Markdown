#!/bin/python3
import sys
import os

def main(argv):
    for i, arg in enumerate(argv):
        if i != 0:
            handleArg(arg)

def handleArg(arg):
    if os.path.isdir(arg):
        handleDir(arg)
    elif os.path.isfile(arg):
        handleFile(arg)

def handleFile(arg):
    f = open(arg, "r");
    keepgoing = True
    x = f.readline()
    while keepgoing:
        x = f.readline()
        keepgoing = x != "---\n"
        if (len(x) == 0):
            print("'" + str(arg) + "'")
            return
    keepgoing = True
    while keepgoing:
        x = f.readline()
        # print(x)
        if x != "---\n" and len(x.strip()) > 0 and x[0] != "#":
            print('"' + arg.replace('"', '\\"') + '"')
            return
        if len(x) == 0:
            return
    
def handleDir(arg):
    fnames = os.listdir(arg)
    for i, name in enumerate(fnames):
        path = os.path.join(arg, name)
        handleArg(path)


if __name__ == "__main__":
    main(sys.argv)
