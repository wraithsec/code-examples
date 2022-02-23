#!/usr/bin/python3
import argparse 
import time
from .utils import cprint
from pathlib import Path

class ls():
    def __init__(self, commandArgs):
        self.path = Path()
        self.parse(commandArgs)
    

    def parse(self, command):
        parser = argparse.ArgumentParser(description='An ls command')
        parser.add_argument('-l', action='store_true', help='Long listing')
        parser.add_argument('-r', action='store_true', help='Recruse')
        parser.add_argument('-t', action='store_true', help='TimeSorted')
        parser.add_argument('path',  nargs='*', default='.', help='paths')
        try:
            args = parser.parse_args(command[1:]) 
            for path in args.path: 
                tpath = Path("".join(path))
                try:
                    if args.l:
                        for child in tpath.iterdir(): 
                            print(
                            self.get_filetype(child),
                            self.convert_chown(child.owner(),child.group()),
                            self.convert_epoch(child.stat().st_mtime),
                            str(child.stat().st_size), 
                            str(child)
                            ) 
                    else:     
                        for child in tpath.iterdir(): print(child) 
                except PermissionError:
                    cprint(f'[-]~ls cannot access file or directory {tpath}: Permission denied')
                except FileNotFoundError:
                    cprint(f'[-]~ls cannot access file or directory {tpath}: Not found')
                print("")
        except SystemExit:
            return 
        return
    
    def get_filetype(self, f):
        if f.is_dir():
            ftype = 'd'
        elif f.is_fifo():
            ftype = 'p'
        elif f.is_socket():
            ftype = 's'
        elif f.is_char_device():
            ftype = 'c'
        elif f.is_block_device():
            ftype = 'b'
        else:
            ftype = '-'
        return ftype

    
    def convert_epoch(self, epoch):
        datetime = time.strftime('%d %b %y %H:%M:%S', time.localtime(epoch))
        return str(datetime)


    def convert_chown(self, owner, group):
        owner = str(owner)
        group = str(group)
        ownerGroup = owner + " " + group 
        return ownerGroup


    def exec(self, args):
        print('Yay!')
        print(args)
        return




        #try:
        #    args = parser.parse_args(command[1:]) 
        #    tpath = Path("".join(args.path))
        #    if args.l:
        #        for child in tpath.iterdir(): print(str(child.owner()),str(child.group()) + ' -- ' + str(child.stat().st_size), str(child.stat().st_mtime) + ' -- ' + str(child)) 
        #    else:     
        #        for child in tpath.iterdir(): print(child) 
        #except SystemExit:
        #    return 
        #return
