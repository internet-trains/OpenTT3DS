#!/usr/bin/env python3

import subprocess
import sys

# ./endian_checker.py <output file> <endian_checker> [endian_force]
popen = subprocess.Popen(sys.argv[2:], stdout=subprocess.PIPE)
popen.wait()

with open(sys.argv[1], 'w+') as output:
    output.write(popen.stdout.read())

