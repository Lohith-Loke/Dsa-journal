#!/usr/bin/env python


def printknapSack(W, wt, val, n):
    K = [[0 for w in range(W + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    # stores the result of Knapsack
    res = K[n][W]
    w = W
    print(f'maxmimum profit :{res}')
    print("items set :", end=":")
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:
            print(wt[i - 1], end=",")
            res = res - val[i - 1]
            w = w - wt[i - 1]
    print()


# value/profit
val = [7, 2, 1, 6, 12]
# weights
wt = [3, 1, 2, 4, 6]
# weight constrain
W = 10
n = len(val)

printknapSack(W, wt, val, n)