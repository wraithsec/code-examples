#!/usr/bin/env python3 

from prompt_toolkit import PromptSession
from colorama import Fore, Back, Style
import sys

printw = lambda x: print(Fore.RED + x + Style.RESET_ALL)
printg = lambda x: print(Fore.GREEN + x + Style.RESET_ALL)

ses = PromptSession('PT & TermColor > ')
while True:
    cmd = ses.prompt('PT & TermColor > ')
    if cmd == "~good":
        printg(cmd)
    elif cmd == "~bad":
        printw(cmd)
    elif cmd.lower() == "~quit":
       printg("[+] Bye!")
       sys.exit()
