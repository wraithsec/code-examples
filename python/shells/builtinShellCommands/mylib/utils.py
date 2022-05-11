#!/usr/bin/python3


class Colors:
    green = '\033[38;5;82m'
    yellow ='\033[38;5;154m'
    red ='\033[38;5;160m'
    blue = '\033[38;5;12m'
    end = '\033[0m'


def cprint(msg):
    if msg.startswith('[+]'):
        print(Colors.green + msg + Colors.end)
    elif msg.startswith('[!]'):
        print(Colors.yellow + msg + Colors.end)
    elif msg.startswith('[-]'):
        print(Colors.red + msg + Colors.end)
    else:
        print("mylib: Unknown error")
