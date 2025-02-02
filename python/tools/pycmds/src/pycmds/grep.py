#!/usr/bin/env python3
from pathlib import Path 
import argparse
import os.path
import glob
import sys
import re

# Add a color highlight?? 
class Color:
    pre = '\033['
    blu = pre + '38;5;033m'
    grn =  pre + '38;5;82m'
    rst = pre + '0m'

def file_path_list(recurse: bool, pathlist: list) -> list:
    moar_files = [] 
    for idx,path in enumerate(pathlist):
        if path.is_dir():
            if recurse:
                moar_files = [file for file in path.rglob('*')] 
            else:
                moar_files = [file for file in path.glob('*')] 
            pathlist.pop(idx)
    pathlist.extend(moar_files)
    return pathlist


def main() -> None:
    parser = argparse.ArgumentParser(description="A crap implementation of grep.")
    parser.add_argument('PATTERN', nargs=1, type=str, help="A extended regular expression for a file. Like grep -E.") 
    parser.add_argument('PATHS', nargs="+", type=Path, help="Files to run regex on.")
    parser.add_argument('-r', '--recurse', dest='r', action='store_true', help="Recurse directories.")
    parser.add_argument('-i', '--nocase', dest='i', action='store_true', help="Regex case insensitivity.")
    parser.add_argument('-l', '--lines-only', dest='l', action='store_true', help="Only return line numbers of matches.")
    args = parser.parse_args()

    rgx = args.PATTERN[0]
    if args.i: 
        rgx = r'(?i)' + rgx
    rgx = re.compile(rgx)

    files = file_path_list(args.r, args.PATHS)
    for file in files:
        with file.open() as f:
            line_count = 0
            for line in f:
                line_count += 1 
                if (suc := rgx.search(line)):
                    if args.l:
                        print(f'{file}{Color.blu}:{line_count}{Color.rst}')
                        continue 
                    print(f'{file}{Color.blu}[{line_count}]{Color.rst}: {line[:suc.start()]}{Color.grn}{line[suc.start():suc.end()]}{Color.rst}{line[suc.end():]}', end='')


if __name__ == "__main__":
    main()
