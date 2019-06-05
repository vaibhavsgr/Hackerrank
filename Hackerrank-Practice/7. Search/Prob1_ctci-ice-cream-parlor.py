#https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    menu = {}
    for i, v in enumerate(cost):
        if money-v in menu:
            print menu[money-v], i+1
        menu[v] = i + 1

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        money = int(raw_input())

        n = int(raw_input())

        cost = map(int, raw_input().rstrip().split())

        whatFlavors(cost, money)
