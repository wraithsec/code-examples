#!/usr/bin/env python3
import subprocess

def myfunc(output: bytes) -> str:
    output = output.decode() 
    return output
    
myfunc(b'bytesobject')
