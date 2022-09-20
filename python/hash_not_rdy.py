#!/usr/bin/env python3
from pathlib import Path
import hashlib
import argparse

def main(algorithims, paths):
    allowed_algos = {
        'md5': hashlib.md5(),
        'sha1': hashlib.sha1(),
        'sha256': hashlib.sha256(),
        'sha512': hashlib.sha512(),
    }

    for path in paths:
        if not Path(path).is_file():
            
    return



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', metavar='ALGORITHIM', required=True, type=lambda lst: [i for i in lst.split(',')] )
    parser.add_argument('paths', metavar='PATHS', nargs='+')
    args = parser.parse_args()
    main(args.a, args.paths)
