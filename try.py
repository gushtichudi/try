#!/usr/bin/python

# script version, refer to version section in readme for how i declare versions for all my scripts/programs

# in short, for each logic of this script that i can implement, the last number of the version gets
# incremented by one, if it hits 5, it resets and increments the middle number of the version by one.
#   ... and vice versa

# e.g.: (2 logics implemented): 0.0.2
#       (4 logics implemented): 0.0.4
#       (8 logics implemented): 0.1.2
#      (16 logics implemented): 0.4.0

# if all logic is implemented, everything will reset and first number of version will increment by one.
# after that, previously explained explanations apply to issues, bugfixes etc

VERSION = "1.0.0"

import time
import subprocess
import os
from sys import argv, exit

argc = len(argv)

if argc < 2:
    print("What do I even do?")
    exit(1)

# arguments after argv[2] is what the user wants to try brute forcing
cmdline = argv[1:]

(fails, status) = (0, 0)
success = False
cooldown_default = 2

while not success:
    print(f"luhphr3ii's try - v{VERSION}\n")

    return_code = subprocess.run(cmdline, stdout=subprocess.PIPE).returncode

    if return_code != 0:
        fails += 1

        print(f"\n!!!!!!!! FAILS :: {fails} !!!!!!!!!!\n")
        print(f"trying again in {cooldown_default} seconds...")

        time.sleep(cooldown_default)

        os.system("clear")
        continue

    print(f"returned: {return_code}")
    print(f"    type: {type(return_code)}")

    # at this point success is seen by you
    success = True

    if success:
        break
