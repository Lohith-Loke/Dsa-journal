#   matrix spiral
from __future__ import barry_as_FLUFL
from operator import le


def lr(l, r, iy, jx):
    for i in range(l, r):
        print(iy, jx)
        jx += 1


A = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
]

t, b, l, r = 0, 0, 0, 0
top = left = 0
bottom = len(A) - 1
right = len(A[0]) - 1
res = []
while True:
    if left > right:
        break
    for i in range(left, right+1):
        print(A[top][i])
        res.append(A[top][i])
    top += 1

    if top > bottom:
        break
    for i in range(top, bottom+1):
        print(A[i][right])
        res.append(A[i][right])
    right -= 1

    if left > right:
        break

    for i in range(right, left-1, -1):
        print(A[i][right])
    bottom = bottom-1

    if top > bottom:
        break

    for i in range(bottom, top-1, -1):
        print(A[i][left])
        res.append(A[i][left])
    left = left+1

print(res)
