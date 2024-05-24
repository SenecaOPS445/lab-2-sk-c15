#!/usr/bin/env python3

#Author: Sandip K C
#Author ID: sk-c15
#Date Created: 2024/05/23

import sys

if len(sys.argv) != 2:
    print("Usage: " + sys.argv[0] + " count")
    sys.exit(1)

timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")