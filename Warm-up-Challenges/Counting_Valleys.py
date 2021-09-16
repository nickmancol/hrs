#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    if steps < 2 or steps > 1000000:
        return 0
    v = [1 if x == 'U' else -1 for x in path]
    valleys = []
    high = 0 
    for s in v:
        if high == 0 and high + s < 0:
            valleys.append(1)
        high += s
        
    return len(valleys)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()