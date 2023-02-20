#!/usr/bin/env python

from numpy import append


def lis(arr: list):
    n = len(arr)
    lst = [[] for i in range(n)]
    lst[0].append(arr[0])

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and (len(lst[i]) < len(lst[j]) + 1):
                lst[i] = lst[j].copy()
        lst[i].append(arr[i])

    maxx = lst[0]

    for x in lst:
        if len(x) > len(maxx):
            maxx = x
    print(" length of LIS is :", len(maxx))
    print(" LIS is :", end=":")

    for i in maxx:
        print(i, end=" ")
    print()


if __name__ == "__main__":
    arr = []
    s = input("enter array :").split(' ')
    for i in s:
        if i.isdigit():
            arr.append(int(i))
    lis(arr)