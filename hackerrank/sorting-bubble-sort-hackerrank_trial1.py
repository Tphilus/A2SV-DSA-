#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    n = len(a)
    numSwap = 0
    
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
                numSwap += 1
    
    firstElement = a[0]
    lastElement = a[-1]
    
    print(f"Array is sorted in {numSwap} swaps.")
    print(f"First Element: {firstElement}")
    print(f"Last Element: {lastElement}")
    


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
