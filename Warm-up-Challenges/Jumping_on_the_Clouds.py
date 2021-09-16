#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    sol = []
    step = 0
    while step <= len(c):
        if step < len(c) - 2:
            if c[step+2] == 0:
                sol.append((step, step+2))
                step = step + 2
            else: 
                sol.append((step, step+1))
                step = step + 1
        elif step < len(c) - 1:
            if c[step+1] == 0:
                sol.append((step, step+1))
                step = step + 1
        else:
            break
        print(step, sol)
    
    return len(sol)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()