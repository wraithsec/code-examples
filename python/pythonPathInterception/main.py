#!/usr/bin/env python3 
import subprocess
from utils import myfunc


def main(): 
    output = subprocess.run('ls -l'.split(), stdout=subprocess.PIPE)
    transformed_output = myfunc(output.stdout)
    print(transformed_output)
    


if __name__ == "__main__":
    main()
