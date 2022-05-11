#!/usr/bin/python3
from __future__ import unicode_literals
from prompt_toolkit import PromptSession
from shlex import split
from mylib.utils import cprint, Colors
import mylib.cmds as cmd
import argparse
import readline
import subprocess
import sys


class Shell:
    def __init__(self):
        self.prompt =  '\x01' + Colors.blue + '\x02' + ' myshell ' + '\x01' + Colors.end + '\x02' + '> '
        self.commands = {}


    def start_shell(self):
        readline.parse_and_bind('tab: complete')
        readline.set_auto_history(True)
        try:
            readline.read_history_file('.shell_hist')
        except:
            pass
        while True:
            cmd = input(self.prompt)
            if cmd.startswith("~"):
                self.builtin_commands(cmd)
            else:
                cprint("[!] Onbox command!") 
                result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
                print(result.stdout.decode('utf-8'))
    


    def builtin_commands(self, builtin):
        builtin = split(builtin)
        if "~quit" in builtin[0]:
            cprint("[+] Quitting!")
            sys.exit()
        elif "~ls" in builtin[0]:
            cmd.ls(builtin)    
        else:
            msg = f'[-] {builtin[0]} is not a builtin command!'
            cprint(msg)
        return 


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A shell with commands')
    parser.add_argument('-s', action='store_true', help="This starts a shell")   
    args = parser.parse_args() 
    if args.s == True:
        shell = Shell() 
        shell.start_shell()

