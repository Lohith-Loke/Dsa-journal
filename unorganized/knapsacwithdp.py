#!/usr/bin/env python3
def pathtrace(res: int, n, w,K):
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:
            print(K[i - 1], end=",")
            res = res - val[i - 1]
            w = w - wt[i - 1]

def solution(W: int, val: list, wt: list, n: int) -> int:
    # print(W)
    if W <= 0 or n == 0:
        # no space or no elements left
        return 0
    if res[n][W] != -1:
        # if data is computed return result
        return res[n][W]

    # bag can hold more
    if wt[n - 1] <= W:
        obj_taken = val[n - 1] + solution(W - wt[n - 1], val, wt, n - 1)
        obj_not_taken = solution(W, val, wt, n - 1)
        res[n][W] = max(obj_taken, obj_not_taken)
        return res[n][W]
    else:
        res[n][W] = solution(W, val, wt, n - 1)
        return res[n][W]


# if __name__ == "__main__":

val = [6, 2, 4]
wt = [1, 2, 3]
W = 10
n = len(val)
z = [-1] * (W + 1)
res = [z for i in range(n + 1)]
x = solution(W, val, wt, len(val))
pathtrace(x, n, W,res)
print(f'Max profit is :{x}')



