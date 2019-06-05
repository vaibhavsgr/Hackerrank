#https://www.hackerrank.com/challenges/swap-nodes-algo/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search&h_r=next-challenge&h_v=zen

from __future__ import print_function

import os
import sys

#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    indexes = []

    for _ in xrange(n):
        indexes.append(map(int, raw_input().rstrip().split()))

    queries_count = int(raw_input())

    queries = []

    for _ in xrange(queries_count):
        queries_item = int(raw_input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
