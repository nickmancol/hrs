#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    st = sorted(arr)
    swaps = 0
    while st != arr:
        for s,v in enumerate(arr):
            if s+1 != v:
                tmp = arr[v-1]
                arr[v-1] = v
                arr[s] = tmp
                swaps +=1
    return swaps
    
            
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()