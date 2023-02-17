#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    res = []
    a1=b1 = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            a1 += 1
        elif a[i] < b[i]:
            b1 += 1
    res = [a1, b1]
    return res


# Write your code here

#a = list(map(int, input().rstrip().split()))

#b = list(map(int, input().rstrip().split()))

a = [1,2,3]
b = [0,3,4]

result = compareTriplets(a, b)
print(result)

