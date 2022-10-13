#!/usr/bin/env python3
'''
Use to setup a venv totally within python. 
'''
from pathlib import Path 
import subprocess
import sys

def main(dank_ascii):
    venv_name = 'venv-test'
    venv_cmd = f'python3 -m venv {venv_name}'.split()
    venv_bin = Path(f'./{venv_name}/bin/python3').absolute()
    venv_path = str(venv_bin.parent)
    venv_bin = str(venv_bin)
    pip_cmd = f'{venv_bin} -m pip install -r ./requirements.txt'.split()

    if not Path(venv_name).exists():
        subprocess.check_call(venv_cmd)
        print(f'\u001b[32;1m[+]\u001b[0m Made new virtual env at {Path(venv_name).absolute()}')
    else: print(f'\u001b[32;1m[+]\u001b[0m {Path(venv_name).absolute()} already exists')
    subprocess.check_call(pip_cmd)
    subprocess.check_call(['clear'])
    print(dank_ascii.center(24))
    print(f'\u001b[32;1m[+]\u001b[0m Virtual environment path: {venv_path}')
    print(f'\u001b[32;1m[+]\u001b[0m All done! Read the README.md and then run the following commands below to get FoulHarvest started.')
    print(f'Run:\n\t. {venv_name}/bin/activate\n\tpython3 my_app.py')
    return

if __name__ == '__main__':
    main(dank_ascii)
