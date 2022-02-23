from __future__ import unicode_literals
import readline 
import sys


class Colors:
    GREEN='\033[32m'
    LIME='\033[92m'
    RED='\033[91m'
    ENDC = '\033[0m'
    newblue = '\033[38;5;87m'
    newgreen = '\033[38;5;82m'

readline.parse_and_bind('tab: complete') 
readline.set_auto_history(True)
try:
    readline.read_history_file('.shell_hist')
except:
    print(Colors.RED + '[!] Problem reading history file!' + Colors.ENDC)


while True:
    cmd = input('\x01' + Colors.newgreen + '\x02' + 'PROMPT > ' + '\x01' + Colors.ENDC + '\x02')
    try:
        if cmd.lower() == '~quit':
            readline.write_history_file('.shell_hist') 
            print(Colors.GREEN + '[+] Okay! Shutting down!' + Colors.ENDC)
            print(Colors.LIME + '[+] Okay! Shutting down!' + Colors.ENDC)
            print(Colors.newgreen + '[+] Okay! Shutting down!' + Colors.ENDC)
            sys.exit()
    except KeyboardInterrupt:
            readline.write_history_file('.shell_hist')
            sys.exit()
