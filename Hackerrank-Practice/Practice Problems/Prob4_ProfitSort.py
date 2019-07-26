"""Given profits of a company for N days and Q queries. Each query contains two 
 integers L and R. For each query, print the number of days on which the profit is
 greater than or equal to L and less than or equal to R. Soln: Sort the profits,
  and for each query, use binary search to find the upper-bound for R and
  lower-bound for L. Time Complexity: O(nlogn + Q)"""
