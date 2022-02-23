#!/usr/bin/env python3 
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory 
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.shortcuts import ProgressBar 
from prompt_toolkit.styles import Style
import time 
import sys

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


shell = PromptSession() 
shell = PromptSession(history=FileHistory('.shell_hist'))

def some_iterable():
    l = list(range(230))
    yield l

while True:
    input = shell.prompt(prompt, style=style, auto_suggest=AutoSuggestFromHistory())
    if input.lower() == '~download':
        prog = some_iterable()
        with ProgressBar() as pb:
            for i in pb(prog):
                time.sleep(0.1) 
    elif input.lower() == '~say_hello':
        print("Hello!") 
    elif input.lower() == '~quit':
        print("Seeya later gator!")
        sys.exit()
    else:
        print(f'OUTPUT of {input}') 
