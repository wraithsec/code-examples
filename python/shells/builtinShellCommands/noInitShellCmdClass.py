#!/usr/bin/env python3
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.shortcuts import ProgressBar
from prompt_toolkit.styles import Style
import argparse
import time

class Cmds:
    def do_help(argslist):
        statement = '''
        "~help - Returns Help
        ~download - Downloads a file
        ~hello - Says hello to you
        ~quit - Whatcha think...
        '''
        print(statement)
        return 1 
    
    def do_download(arglist):
        parser = argparse.ArgumentParser(description='A download command.')
        parser.add_argument('filename', nargs='*', help='Paths')
        try:
            args = parser.parse_args(arglist)
        except SystemExit:
            return 1
        prog = range(250)
        with ProgressBar() as pb:
            for i in pb(prog):
                time.sleep(0.001) 
        return 1

    def do_hello(arglist):
        parser = argparse.ArgumentParser(description='A hello command.')
        parser.add_argument('name', nargs='*', help='The names you want to say hello to.')
        try:
            args = parser.parse_args(arglist)
        except SystemExit:
            return 1
        [ print(f"Hello {name}!") for name in args.name ]
        return 1
    
    def do_quit(arglist):
        print("Seeya later gator!")
        exit()
        return 1 

def get_builtins():
    builtins_dict = {}
    for k, v in Cmds.__dict__.items():
        if k.startswith('do_'):
            builtins_dict[k] = v
    return builtins_dict

if __name__ == "__main__": 
    shell = PromptSession() 
    shell = PromptSession(history=FileHistory('.shell_hist'))
    builtins = get_builtins()

    while True:
        INPUT = shell.prompt("A-PROMPT > ", auto_suggest=AutoSuggestFromHistory())
        if INPUT.startswith('~'):
            INPUT = INPUT.split()
            ARGS = INPUT[1:]
            CMD = 'do_' + INPUT[0].lstrip('~')
            if CMD in builtins:
                OUTPUT = builtins.get(CMD)(ARGS)
            else:
                print(f'[!] Builtin {INPUT[0]} does not exist!!!!')
        else:
            print(f'OUTPUT of {INPUT}') 
