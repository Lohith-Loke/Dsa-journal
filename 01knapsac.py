#!/usr/bin/env python

# This is the memoization approach of
# 0 / 1 Knapsack in Python in simple
# we can say recursion + memoization = DP



def knapsack(wt, val, W, n):

    # base conditions
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]

    # choice diagram code
    if wt[n - 1] <= W:
        t[n][W] = max(val[n - 1] + knapsack(wt, val, W - wt[n - 1], n - 1),
                      knapsack(wt, val, W, n - 1))
        return t[n][W]
    elif wt[n - 1] > W:
        t[n][W] = knapsack(wt, val, W, n - 1)
        return t[n][W]


# driver code
val = [200, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
# make matrix of W+1 x n  with -1
z = [-1] * (W + 1)
res = []
for i in range(n + 1):
    res.append(z)

t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
print(knapsack(wt, val, W, n))

# This code is contributed by Prosun Kumar Sarkar
