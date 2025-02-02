#!/usr/bin/env python3
from pathlib import Path
import hashlib
import argparse
'''
Simple attemtp at making a multipurpose hash script in Python. Just got curious.
'''


def main(algorithims: str = None, paths: str = None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', metavar='ALGORITHIMS', type=lambda lst: [i for i in lst.split(',')], default=['md5'], help="Choose one or more of md5, sha1, sha256, sha512" )
    parser.add_argument('paths', metavar='PATHS', nargs='+', type=Path)

    args = parser.parse_args()
    print(args)
    algorithims = args.a
    paths = args.paths

    allowed_algos = [ 'md5', 'sha1', 'sha256', 'sha512' ]

    for path in paths:
        print()
        if not path.is_file(): 
            print(f'[-] {path} not a file!')
        else: 
            for a in algorithims: 
                if a not in allowed_algos:
                    print(f'[-] {a} not a known algorithim.')
                else:
                    alg = hashlib.new(a)
                    alg.update(path.read_bytes())
                    print(f'[+] {alg.hexdigest()}\t{path}')
    return


if __name__ == "__main__":
    main()
