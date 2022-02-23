from prompt_toolkit import PromptSession
from termcolor import cprint 

printw = lambda x: cprint(x, 'white', 'on_red', attrs=['blink']) 
printg = lambda x: cprint(x, 'green') 

ses = PromptSession('PT & TermColor > ')
while True:
    cmd = ses.prompt('PT & TermColor > ')
    if cmd == "~yay":
        printg(cmd)
    elif cmd == "~boo":
        printw(cmd)
