#!/usr/bin/evn python3
import psutil
import datetime

def main(args: list) -> None:
    for proc in psutil.process_iter():
        if proc.pid in (7607, 7635, 2609):
            print("------------------------------------")
            print(f"CMDLINE: {' '.join(proc.cmdline())}")
            print(f"NAME: {proc.name()}")
            print(f"PID: {proc.pid}")
            print(f"PPID: {proc.ppid()}")
            print(f"USER: {proc.username()}")
            print(f"START: {datetime.datetime.fromtimestamp(proc.create_time()).strftime('%c')}")
            print(f"CWD: {proc.cwd()}")
            print("------------------------------------")
    else:
        print("No pids match!") 
    return

if __name__ == '__main__':
    main()
