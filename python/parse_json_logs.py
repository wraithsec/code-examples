#!/usr/bin/env python3
'''
Script used to make json logs from cowrie more readable. 
'''

from datetime import date
import json
import os
import sys

os.setuid(1000)

#Need to add the ability to select this. 
cowrie_json = '/home/cower/cowrie/var/log/cowrie/cowrie.json'
readable_json = f'/home/cower/cowrie/var/log/cowrie/{date.today()}.readable.cowrie.log'

if os.path.exists(readable_json):
    while True:
        c = input(f"[!] Output file {readable_json.split('/')[-1]} already exists! Delete and start fresh?? [N]|y: ") or 'N'
        if c.lower() == 'y':
            os.remove(readable_json)
            print(f"[+] Deleted {readable_json}")
            break
        elif c.lower() == 'n':
            print("[ ] Okay exiting for now")
            sys.exit()
        else:
            print("[!] Choose a valid choice!")
            continue


with open(cowrie_json) as f:
    print(f"[ ] Parsing {cowrie_json.split('/')[-1]} now!")
    keys = ['timestamp', 'session', 'src_ip', 'message']
    for line in f:
        data = json.loads(line)
        output_line = [data.get(key) for key in keys]
        out_string = f"{' | '.join(output_line[0:3])}: {output_line[-1]}\n"
        with open(readable_json, 'a') as n:
            n.write(out_string)
    print(f"[+] Log parsed and at {readable_json}")

