#!/usr/bin/env python3
from pathlib import Path
import os
import argparse 
import datetime
import stat



class ls_cmd:
    def run():
        args = ls_cmd.parse_args()
        output = ls_cmd._run_cmd(args)
        ls_cmd._parse_output(args, output)
        return 

    def parse_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('-l', action='store_true', help='Long listing.')
        parser.add_argument('-a', action='store_true', help='Show all files, including hidden.')
        parser.add_argument('-t', action='store_true', help='Sort by mtime.')
        parser.add_argument('-r', action='store_true', help='Reverse sort order.')
        parser.add_argument('-R', action='store_true', help='Recursive')
        parser.add_argument('files', nargs='+')
        return parser.parse_args()

    def _parse_uid_gid() -> tuple[dict, dict]:
        pdict = {} 
        passwd = Path('/etc/passwd')
        with passwd.open('r') as f:
            pdict.update( [(int(line.split(':')[2]), line.split(':')[0]) for line in f if not line.startswith('#')] )
        
        gdict = {}
        groups = Path('/etc/group')
        with groups.open('r') as f:
            gdict.update( [(int(line.split(':')[2]), line.split(':')[0]) for line in f if not line.startswith('#')] )
        return pdict, gdict

    def _run_cmd(args):
        output = []
        for file in args.files:
            file_name = Path(file)
            file_metadata = file_name.stat()
            output.append({"name": file_name, "data": file_metadata})
        return output

    def _parse_output(args, files: list):
        if args.t: 
            files = sorted(files, key=lambda x: x.get('data').st_mtime)
        if args.r:
            files = files[-1:0]
        output = []
        if args.l:
            total = len(files)
            output.append(f"total {total}\n")
            passwd, groups = ls_cmd._parse_uid_gid()
            for file in files:
                name = file.get('name')
                perms = stat.filemode(file.get('data').st_mode)
                mtime = datetime.datetime.fromtimestamp(int(file.get('data').st_mtime)).strftime('%b %e %H:%M')
                atime = datetime.datetime.fromtimestamp(int(file.get('data').st_atime)).strftime('%b %e %H:%M')
                ctime = datetime.datetime.fromtimestamp(int(file.get('data').st_ctime)).strftime('%b %e %H:%M')
                inode = file.get('data').st_ino
                uid = passwd.get(file.get('data').st_uid) or file.get('data').st_uid
                gid = groups.get(file.get('data').st_gid) or file.get('data').st_gid
                size = file.get('data').st_size
                links = file.get('data').st_nlink
                file = f'{perms} {links} {uid}\t{gid}\t{size:>4} {mtime} {name}\n'
                output.append(file)
            print(''.join(output))
        else:
            col = os.get_terminal_size().columns
            for file in files:
                filename = file.get('name')
                output.append(f"{filename}\t")
            print('\t'.join(output))
        return
    

if __name__ == "__main__":
    ls_cmd.run()