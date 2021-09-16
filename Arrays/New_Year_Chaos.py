#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    tc = 'Too chaotic'
    bribes = 0
    nq = [n-1 for n in q]
    for s,v in enumerate(nq):
        cb = s-v
        if cb <-2:
            bribes = tc
            break
        for i in range(max(v-1,0),s):
            if nq[i] > v:
                bribes += 1
    print(bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)