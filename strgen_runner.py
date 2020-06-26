#!/bin/env python3

import subprocess
import sys

# ./strgen_runner.py <strgen> <strgen args>
popen = subprocess.Popen(sys.argv[1:], stdout=subprocess.PIPE)
sys.exit(popen.wait())