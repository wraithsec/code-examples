#!/usr/bin/python3 
import psutil, datetime, argparse
import pandas as pd 

'''This works.. but not in the way I'd like. I want to make it so certain fields appear first. This also shows ALL output.. so gotta figure that out. And getting rid of the left field is important''' 

def get_pslist():
    pslist = {p.pid: p.info for p in psutil.process_iter(['pid', 'ppid', 'create_time', 'username', 'terminal', 'exe', 'name', 'cmdline'])}
    #for proc in psutil.process_iter(['pid', 'ppid', 'create_time', 'username', 'terminal', 'name', 'cmdline']):
    #    print(proc.info)
    pids = [pid for pid in psutil.pids()]
    return pids  

def get_pslist2(pids):
    proccesslist = []
    for pid in pids:  
        p = psutil.Process(pid)
        pdict = p.as_dict(attrs=['username', 'pid', 'ppid', 'gids', 'status', 'create_time', 'name', 'cmdline'])
        pdict['gids'] = pdict['gids'].real
        pdict['create_time'] = datetime.datetime.fromtimestamp(pdict['create_time']).strftime('%Y-%m-%d %H:%M:%S')
        pdict['cmdline'] = ' '.join(pdict['cmdline'])
        print(pdict)
        proccesslist.append(pdict)
    return processlist

def get_pslist1(pids):
    processlist = []
    for pid in pids:
        p = psutil.Process(pid)
        with p.oneshot():
            [ 
            p.username(),
            p.pid,
            p.ppid(),
            p.gids().real,
            p.status(),
            datetime.datetime.fromtimestamp(p.create_time()).strftime('%Y-%m-%d %H:%M:%S'),
            p.name(), " ", 
            " ".join(p.cmdline())
            ]
    return processlist

def show_names():
    pslist = get_pslist()  
    pd.set_option('display.max_rows', None)
    df = pd.DataFrame().T
    df.fillna(0, inplace=True) 
    print(df) 
    return

def main(args): 
    if args.name:
        pids = get_pslist2([1])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', help="Show all process names and pids", action="store_true")
    args = parser.parse_args()
    main(args)

    
