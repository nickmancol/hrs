#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    i = 0
    sums = []
    while i < len(arr)-2:
        j = 0
        while j < len(arr)-2:
            hg1 = (arr[i][j],arr[i][j+1],arr[i][j+2])
            hg2 = (arr[i+1][j+1])
            hg3 = (arr[i+2][j],arr[i+2][j+1],arr[i+2][j+2])
            sums.append(sum(hg1)+hg2+sum(hg3))
            j += 1
        i += 1
    return max(sums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
