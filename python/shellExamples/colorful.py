##Colorful
from prompt_toolkit import PromptSession
import colorful as cf 
import sys

cf.use_true_colors()
cf.update_palette({
    'mint': '#c5e8c8',
    'purp': '#4d0078'
})


printw = lambda msg: print(cf.white_on_red(msg))
printg = lambda x: print(cf.cyan(x))
printm = lambda x: print(cf.purple(x))
printb = lambda x: print(cf.orange(x))

ses = PromptSession('PT & TermColor > ')
while True:
    cmd = ses.prompt('PT & TermColor > ')
    if cmd.lower() == "~good":
        print(cmd)
        print(cf.cyan_on_slateGray('[*] Wow, this is actually mint'))
        printg("Yay")
    elif cmd.lower() == "~bad":
        print(cmd)
        printm(cmd)
        print(cf.purp(cmd))
    elif cmd.lower() == "~quit":
        print(cmd)
        printb("[+] Bye bye!")
        sys.exit()
    else:
        printw("Not a command! Try again!") 
