
from ast import Return
from tkinter.messagebox import RETRY


def binarysearh(a, ele):
    high = len(a)-1
    low = 0
    while high > low:
        mid = low+int((high-low)/2)
        if a[mid] == ele:
            return mid
        else:
            if a[mid] > ele:
                low = mid+1
            else:
                high = mid-1
    return -1


a = [1, 2, 4, 6, 8, 8, 9]
res = binarysearh(a, 5)
print(res)
