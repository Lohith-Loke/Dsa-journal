#!/usr/bin/python
import random

class Sol():
    def max_area(self, a, maxarr=-1):
        b = 1000
        index = -1
        for i in range(len(a)):
            if b > a[i]:
                # first occure of min is only used
                b = a[i]
                index = i
        area = b*len(a)
        maxarr = max(area, maxarr)
        p1 = a[index+1:]
        p2 = a[:index]
        if p1:
            maxarr = self.max_area(p1, maxarr)
        if p2:
            maxarr = self.max_area(p2, maxarr)
        return maxarr

    def max_perm(self, a, maxprem=-1):
        b = min(a)
        index = a.index(b)
        perm = 2*(b+len(a))
        maxprem = max(perm, maxprem)
        p1 = a[index+1:]
        p2 = a[:index]
        if p1:
            maxprem = self.max_perm(p1, maxprem)
        if p2:
            maxprem = self.max_perm(p2, maxprem)
        return maxprem


s = Sol()

b = []

for i in range(100):
    b.append(random.randint(1, 101))

print(s.max_area(b))
print(s.max_perm(b))
