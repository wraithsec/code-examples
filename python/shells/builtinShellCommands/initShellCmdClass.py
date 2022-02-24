#!/usr/bin/env python3
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.shortcuts import ProgressBar
from prompt_toolkit.styles import Style
import argparse
import time

class Cmds:
    def __init__(self):
        self.builtins = { 
            '~help': self.help,
            '~download': self.download,
            '~hello': self.hello,
            '~quit': self.bye
        }

    def help(self, arglist):
        statement = '''
        ~help - Returns Help
        ~download - Downloads a file
        ~say_hello - Says hello to you
        ~quit - Whatcha think...
        '''
        print(statement)
        return 1 
    
    def download(self, arglist):
        parser = argparse.ArgumentParser(description='A download command')
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

    def hello(self, arglist):
        parser = argparse.ArgumentParser(description='A hello command')
        parser.add_argument('name', nargs='*', help='The names you want to say hello to.')
        try:
            args = parser.parse_args(arglist)
        except SystemExit:
            return 1
        [ print(f"Hello {name}!") for name in args.name ]
            
        return 1
    
    def bye(self, arglist):
        print("Seeya later gator!")
        exit()
        return 1 


if __name__ == "__main__":
    shell = PromptSession() 
    shell = PromptSession(history=FileHistory('.shell_hist'))
    commands = Cmds()

    while True:
        INPUT = shell.prompt("APROMPT > ", auto_suggest=AutoSuggestFromHistory())
        if INPUT.startswith('~'):
            INPUT = INPUT.split()
            ARGS = INPUT[1:]
            CMD = INPUT[0]
            if CMD in commands.builtins:
                OUTPUT = commands.builtins.get(CMD)(ARGS)
            else:
                print(f'[!] Builtin {INPUT[0]} does not exist!!!!')
        else:
            print(f'OUTPUT of {INPUT}') 

