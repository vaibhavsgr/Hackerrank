"""
Given a value N, if we want to make change for N cents, and we have infinite supply of each of
S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change?
The order of coins doesn’t matter.

For example, for N = 4 and S = {1,2,3},
there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}.
So output should be 4.

For N = 10 and S = {2, 5, 3, 6},
there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}.
So the output should be 5.

SOLUTION

1) Optimal Substructure
To count the total number of solutions, we can divide all set solutions into two sets.
1) Solutions that do not contain mth coin (or Sm).
2) Solutions that contain at least one Sm.
Let count(S[], m, n) be the function to count the number of solutions,
then it can be written as sum of count(S[], m-1, n) and count(S[], m, n-Sm).

Therefore, the problem has optimal substructure property as the problem can be solved using solutions to subproblems.

2) Overlapping Subproblems
Following is a simple recursive implementation of the Coin Change problem.
The implementation simply follows the recursive structure mentioned above.
"""

"""Recursive solution
def CoinChange(N, m, S):
    #Case 1 : if N=0:
    if N == 0:
        return 0

    #case 2 : if N<0 then no solution exist
    if N < 0 :
        return 0

    #case 3 : if no of coins <= 0 and N > 0, no solution exist
    if m < 0 and N > 0:
        return 0

    #case 4 : Solution (a)solution including S[m-1] coin,
    #(b) solution excluding S[m-1] coin
    return CoinChange(N, m-1, S) + CoinChange(N, m, S[m-1])
"""
#DYNAMIC  SOLUTION

def coinChange(coins, value):
    ways = [0]*(value+1)

    for coin in coins:
        if coin > value: #if coin > value, there's no reason to use it
            continue
        ways[coin] += 1 #coin by itself as a set

        for i in range(coin+1,value+1): #fill the remaining sets with a new possibility with this coin
            ways[i] += ways[i-coin]

    print (ways)
    return ways[value]

if __name__ == "__main__":
    coins = [2,5,3,6]
    value = 10
    result = coinChange(coins, value)
    print (result)
