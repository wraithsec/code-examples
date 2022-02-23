#!/usr/bin/python3 
import psutil 
import argparse
import pandas as pd 

'''This works.. but not in the way I'd like. I want to make it so certain fields appear first. This also shows ALL output.. so gotta figure that out. And getting rid of the left field is important''' 

def get_pslist():
    pslist = {p.pid: p.info for p in psutil.process_iter(['pid', 'ppid', 'create_time', 'username', 'terminal', 'environ', 'exe', 'name', 'cmdline'])}
    return pslist 

def show_names():
    pslist = get_pslist()  
    df = pd.DataFrame(pslist).T
    df.fillna(0, inplace=True) 
    print(df) 
    return

parser = argparse.ArgumentParser()
parser.add_argument('--name', help="Show all process names and pids", action="store_true")
args = parser.parse_args()

if args.name:
    show_names()
