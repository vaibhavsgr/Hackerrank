import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    toys = 0
    for price in prices:
        if price <= k:
            toys += 1
            k -= price
        else:
            return toys
    return toys


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print "Enter the number of toys and the amount of money"
    nk = raw_input().split()
    n = int(nk[0])
    k = int(nk[1])
    print "Enter the price of each toy"
    prices = list(sorted(map(int, raw_input().rstrip().split())))
    result = maximumToys(prices, k)
    print result
