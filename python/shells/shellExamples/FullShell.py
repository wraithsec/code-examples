#!/usr/bin/env python3 
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory 
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.shortcuts import ProgressBar 
from prompt_toolkit.styles import Style
import time 

style = Style.from_dict({
    # User input (default text).
    '':          '#ff0066',

    # Prompt.
    'username': '#884444',
    'at':       '#00aa00',
    'colon':    '#0000aa',
    'pound':    '#00aa00',
    'host':     '#00ffff',
    'path':     'ansicyan underline',
})

prompt = [
    ('class:username', 'john'),
    ('class:at',       '@'),
    ('class:host',     'localhost'),
    ('class:colon',    ':'),
    ('class:path',     '/user/john'),
    ('class:pound',    '# '),
]

def some_iterable():
    l = list(range(2500))
    yield l

class Cmds:
    def __init__(self):
        self.builtins = { 
            '~help': self.help_statement,
            '~download': self.download,
            '~hello': self.hello,
            '~quit': self.myquit
        }

    def help_statement():
        statement = '''
        ~help - Returns Help
        ~download - Downloads a file
        ~say_hello - Says hello to you
        ~quit - Whatcha think...
        '''
        print(statement)
        return 1 
    
    def download():
        prog = some_iterable()
        with ProgressBar() as pb:
            for i in pb(prog):
                time.sleep(0.1) 
        return 1

    def hello(name):
        print(f"Hello {name}!") 
        return 1
    
    def myquit():
        print("Seeya later gator!")
        exit()
        return 1 


shell = PromptSession() 
shell = PromptSession(history=FileHistory('.shell_hist'))
commands = Cmds()

while True:
    INPUT = shell.prompt(prompt, style=style, auto_suggest=AutoSuggestFromHistory())
    if INPUT.startswith('~'):
        OUTPUT = commands.builtins.get(INPUT.split()[0])
        if OUTPUT is None:
            print(f'[!] Builtin {INPUT} does not exist!!!!')
        else:
            print(OUTPUT)
    else:
        print(f'OUTPUT of {INPUT}') 
